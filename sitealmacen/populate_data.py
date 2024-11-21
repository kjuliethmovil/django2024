import os
import django
import random
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitealmacen.settings')
django.setup()
from django.contrib.auth.models import User
from Misapps.clientes.models import Cliente
from Misapps.productos.models import TipoProducto, Producto
from Misapps.ventas.models import Venta, VentaProducto

fake = Faker()

def create_clientes(n=10):
    for _ in range(n):
        Cliente.objects.create(
            nombreCliente=fake.name(),
            direccionCliente=fake.address(),
            telefonoCliente=fake.phone_number()[:12],  # Limitar a 12 caracteres
            correoCliente=fake.unique.email(),
            password=fake.password(length=10),
            estado=True
        )

def create_tipo_producto(n=10):
    for _ in range(n):
        TipoProducto.objects.create(
            nombre=fake.word(),
        )

def create_productos(n=20):
    tipos = list(TipoProducto.objects.all())
    for _ in range(n):
        Producto.objects.create(
            nombre=fake.word(),
            marca=fake.company(),
            precio=round(random.uniform(10.0, 100.0), 2),
            stockmin=random.randint(1, 10),
            cantidad=random.randint(1, 100),
            tipoproducto=random.choice(tipos) if tipos else None
        )

def create_ventas(n=100):
    clientes = list(Cliente.objects.all())
    usuarios = list(User.objects.all())
    for _ in range(n):
        Venta.objects.create(
            fecha = fake.date(),
            descuento = round(random.uniform(0.0, 10.0), 2),
            total = round(random.uniform(100.0, 1000.0), 2),
            subtotal = round(random.uniform(90.0, 990.0), 2),
            usuario = random.choice(usuarios),
            #producto = 
            #created = 
            #updated =
            cliente = random.choice(clientes)
        )

def create_venta_productos(n=200):
    ventas = list(Venta.objects.all())
    productos = list(Producto.objects.all())
    for _ in range(n):
        venta = random.choice(ventas)
        producto =random.choice(productos)
        cantidad = random.randint(1, 10)
        VentaProducto.objects.create(
            producto=producto,
            venta=venta,
            fechaVenta=fake.date_time(),
            precio=producto.precio,
            cantidad=cantidad,
            total=round(producto.precio * cantidad, 2)
        )

if __name__ == '__main__':
    print("Creando datos falsos...")
    create_clientes()
    create_tipo_producto()
    create_productos()
    create_ventas()
    create_venta_productos()
    print("Datos falsos creados con exito...")


    #python3 populate_data.py