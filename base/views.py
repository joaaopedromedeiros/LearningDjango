from django.shortcuts import render


# Create your views here.
# Create the app's urls in this app

rooms = [
    {"id": 1, "nome": "Python"},
    {"id": 2, "nome": "front"},
    {"id": 3, "nome": "Design"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, "base/home.html", context) #return render(request, "template.html")

def room(request,pk):
    for i in rooms:
        if i['id'] == int(pk):
            correctroom = i
    room = {'room': correctroom }
    return render(request, "base/room.html", room)

