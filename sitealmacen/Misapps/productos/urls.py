from django.urls import path
#from Apps.productos.views import home
from Misapps.productos.views import get_productos_with_tipoproducto, TipoProductoList, TipoProductoDetail, ProductoList, ProductoDetail, ProductoConTipoList


app_name = "productos"
urlpatterns = [
    path('', ProductoList.as_view()),
    path('<int:pk>', ProductoDetail.as_view()),
    path('tipo-producto/', TipoProductoList.as_view()),
    path('tipo-producto/<int:pk>', TipoProductoDetail.as_view()),
    path('productos-con-tipo/', get_productos_with_tipoproducto, name='productos-con-tipo')
]

