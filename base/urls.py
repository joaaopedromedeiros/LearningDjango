# Eu criei para colocar as urls + views desse app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #path(url, arquivoviews.funçãoimportada, name="nome")
    path('room/<str:pk>',views.room, name="room")
]

# Eu defino a url aqui, pois no urls.py "mãe" eu apenas coloco path('', include("appname.urls")) 
# e ele faz a inclusão de todos os path na url mãe

