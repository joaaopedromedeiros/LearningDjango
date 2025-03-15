from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# we create the datebase table here


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # se apagarem a classe pai, a msg também some, relação de 1 pra 1
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # ele não pode ser vazio, orbigatoriamente vai ser TTrue então precisa ter algo
    #participants =
    updated = models.DateField(auto_now=True) # every time you modify
    created = models.DateField(auto_now_add=True) # quando a gente criou/instanciou a primeira vez

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # se apagarem a classe pai, a msg também some
    body = models.TextField()
    updated = models.DateField(auto_now=True) # every time you modify
    created = models.DateField(auto_now_add=True) # quando a gente criou/instanciou a primeira vez

    def __str__(self):
        return self.body[0:50]
