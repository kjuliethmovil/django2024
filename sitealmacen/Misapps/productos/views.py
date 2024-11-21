from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView

from rest_framework import status

from Misapps.productos.models import TipoProducto, Producto
from Misapps.productos.serializers import TipoProductoSerializer, ProductoSerializer, ProductoListSerializer
#CONSULTAS
from rest_framework.decorators import api_view
from django.db.models import Q
# Create your views here.


class TipoProductoList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    

    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class TipoProductoDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ProductoList(APIView):
   
    def get(self, request, format=None):
        productos = Producto.objects.all()
        # data = {"results": list(clientes.values("nombreCliente", "direccionCliente", "telefonoCliente", "correoCliente", "passwordCliente"))}
        # print(data)
        # return JsonResponse(data)
        serializer = ProductoListSerializer(productos, many=True)
        return Response({"producto":serializer.data})

    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetail(APIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoListSerializer(producto)
        return Response({"producto":serializer.data})

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductoConTipoList(APIView):
    # LISTA DE PRODUCTOS CON EL NOMBRE DEL TipoProducto

   """  def  get(self, request, format=None):
        productos = Producto.objects.select_related('tipoproducto').values(
            'id',  'nombre', 'descripcion', 'precio', 'stokmin', 'tipoproducto__nombre'
        )
        return JsonResponse(list(productos), safe=False) """
    
def get(self, request, format=None):

    productos = Producto.objects.all()
    return JsonResponse(list(productos), safe=False)


#NUEVO

@api_view(['GET'])
def get_productos_with_tipoproducto(request):
    producto = Producto.objects.all()

    """ producto = Producto.objects.filter(
        Q(cantidad__gte=80) &
        Q(marca__icontains="Onela-Parker")
    ) """

    """ cantidad = request.data.get("cantidad", None)
    marca = request.data.get("marca", None)
    consulta = Q()

    if cantidad is not None:
        cantidad &= Q(cantidad__gte = cantidad)
    if marca is not None:
        marca &= Q(marca__icontains = marca)
 """
    #serializador 
    serializer = ProductoSerializer(producto, many=True)
   #productos con condiciones body
   



    return Response(serializer.data)











       
