from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


# Create your views here.
# Create the app's urls in this app

#rooms = [
#    {"id": 1, "nome": "Python"},
#    {"id": 2, "nome": "front"},
#    {"id": 3, "nome": "Design"},
#]


# tenho as funções com o back-end e lógica, os valores e variáveis que são passados para o front que vem dos models cadastrados 

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "base/home.html", context) #return render(request, "template.html")



def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room } #variável acessada é room
    return render(request, "base/room.html", context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_forms.html", context)


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

def delete_room(request, pk): # Aqui ele coloca a url como argumento e o parametro que passei depois
    rooom = Room.objects.get(id=pk)
    rooom.delete()
    return render(request, 'base/home.html')



