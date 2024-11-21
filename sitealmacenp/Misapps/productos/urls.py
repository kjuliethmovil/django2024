from django.urls import path
#from Apps.productos.views import home
from Misapps.productos.views import TipoProductoList, TipoProductoDetail, ProductoList, ProductoDetail


app_name = "productos"
urlpatterns = [
    path('', ProductoList.as_view()),
    path('<int:pk>', ProductoDetail.as_view()),
    path('tipo-producto/', TipoProductoList.as_view()),
    path('tipo-producto/<int:pk>', TipoProductoDetail.as_view()),
]

