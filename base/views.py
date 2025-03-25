from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from .models import *


# Create your views here.
# Create the app's urls in this app

#rooms = [
#    {"id": 1, "nome": "Python"},
#    {"id": 2, "nome": "front"},
#    {"id": 3, "nome": "Design"},
#]


# tenho as funções com o back-end e lógica, os valores e variáveis que são passados para o front que vem dos models cadastrados 

def LoginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get("password")

        try: 
            user = User.objects.get(username=username) # verifica se o usuário existe, se der erro aparece aquela mensagem. Sem o try quebra
        except:
            messages.error(request, "Use dosent exists")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password dosent exist")

    context = {'page': page}
    return render(request, 'base/login_register.html', context )


def LogoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm() #depois usa o {{form.as_p}}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"Ocorreu um erro durante o registro")

    context = {'form': form} 
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q')  if request.GET.get('q') != None else ''  
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |  
        Q(name__icontains=q) |
        Q(description__icontains=q)
        ) 
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'rooms_count': rooms_count, } # dicionário {'VariavelQuePodeAcessarNoHtml': VariavelDoViews}
    return render(request, "base/home.html", context) #return render(request, "template.html", variável de acesso aos dados)



def room(request,pk):
    room = Room.objects.get(id=pk)
    room_massages = room.message_set.all().order_by('-created') # give the set of massages tha is related to the specific room
    # para a relação acima precisei usar o set_all(), mas abaixo que usa muitos para muitos posso apenas chamar com o atributo mesmo.
    # A relação é diferente no modal, ao criar o atributo
    participantes = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")

        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)




    context = {'room': room, 'room_massages': room_massages, 'participants': participantes } #variável acessada é room
    return render(request, "base/room.html", context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_forms.html", context)

@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # esse instance faz preencher os dados do forms de acordo com os dados do modal de pk


    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
             form.save()
             return redirect('home')

    context = {'form': form}
    return render(request,'base/room_forms.html', context)


@login_required(login_url='login')
def delete_room(request, pk): # Aqui ele coloca os elementos passados da formtação da url como argumento 

    rooom = Room.objects.get(id=pk)

    if request.user != rooom.host:
        return HttpResponse('Your are not allowed here!!')
    
    rooom.delete()
    return redirect('home')



# Ele renderiza com o views e  url inciais da home
# Ele com os argumentos passados pelo html por via do href ou forms, ele vai para URL DO SITE 
# Os dados dessa URL  viram argumentos para uma views
# A views executa toda lógica do back e retorna alguma ação e valor dentro da variável


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')
    
    message.delete()

    
    return redirect('home')


