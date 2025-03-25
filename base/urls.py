# Eu criei para colocar as urls + views desse app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #path(url, arquivoviews.funçãoimportada, name="nome")
    path('room/<str:pk>',views.room, name="room"), # <str:parametro>, <int:parametro>, recebe o argumento do banco de dados
    path('create-room',views.create_room, name="create-room"),
    path('update-room/<str:pk>/',views.update_room, name="update-room"),
    path('delete-room/<str:pk>/', views.delete_room, name="delete-room"),
    path('login/', views.LoginPage, name="login"),
    path('logout/', views.LogoutUser, name="logout"),
    path('registro/', views.registerPage, name="registro"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-mensagem"),

    # cria a formatação do parametro de como chega o argumento para o request da url nesse caso --> ('delete-room'); A URL É ARGUMENTO DE REQUEST QUE TA EM VIEWS
    # cria a formtação do parametro  de como o argumento de pk vai ser recebido (/<str:pk>/); --> PK É ARGUMENTO DO PARAMETTRO PK QUE TA EM VIEWS
   
    # É como se na views eu definisse os parametros para executar a função assim que entra na url, e no html quais argumentos irão vim pelo href
    # e aqui eu digito a formatação de envio dos parametros que vai enviar os argumentos para views 

    # render html, request com views + urls (tela inicial)
    # html --> href --> urls argumentos passadoos pra views --> views --> executa o que precisar 
]

# Eu defino a url aqui, pois no urls.py "mãe" eu apenas coloco path('', include("appname.urls")) 
# e ele faz a inclusão de todos os path na url mãe

