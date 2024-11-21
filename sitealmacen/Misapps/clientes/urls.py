from django.urls import path
from Misapps.clientes.views import home
from Misapps.clientes.views import ClienteList, ClienteDetail


app_name = "clientes"
urlpatterns = [
    #path('', home, name= 'home'),
    path('', ClienteList.as_view()),
    path('<int:pk>', ClienteDetail.as_view()),
]

