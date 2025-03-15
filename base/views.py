from django.shortcuts import render
from .models import Room
from .forms import RoomForm


# Create your views here.
# Create the app's urls in this app

#rooms = [
#    {"id": 1, "nome": "Python"},
#    {"id": 2, "nome": "front"},
#    {"id": 3, "nome": "Design"},
#]



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
    context = {'form': form}
    return render(request, "base/room_forms.html", context)



