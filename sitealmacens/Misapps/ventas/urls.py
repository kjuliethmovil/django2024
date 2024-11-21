from django.urls import path
from Misapps.ventas.views import VentaList, VentaDetail

app_name = "clientes"
urlpatterns = [
    path('', VentaList.as_view()),
    path('<int:pk>', VentaDetail.as_view()),

]