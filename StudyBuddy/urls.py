
from django.contrib import admin
from django.urls import path, include

#from django.http import HttpResponse
# Essas funções são caracterizados como VIEWS, e nelas existem várias lógicas em programas grandes, 
# por isso o django tem um arquivo separada apenas para elas, para não ficar todas aqui, por isso vários apps com views e models 
# específicos
# -------------------------------- views ---------------
#def home(request):
#    return HttpResponse("Hello World")

#def room(request):
#    return HttpResponse("room")

#def room2(request):
#    return HttpResponse("room 1")
# -------------------------------- fim views ---------------

# Aqui é as urls gerais

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home), #como é a home não tem /
    #path('room/', room), #não tem o /room, o "/" já tem escondido
    #path('room/2', room2)
    path('',include("base.urls"))
]



# para vincular as urls e views de um app usamos o include no import
# path('', include("nomedapastadoapp.arquivourls"))
