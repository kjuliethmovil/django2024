from django.contrib import admin
from Misapps.clientes.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombreCliente', 'direccionCliente', 'telefonoCliente', 'correoCliente')
    ordering = ('nombreCliente', 'direccionCliente', 'correoCliente')  # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('nombreCliente','correoCliente') #Campo relacionado

    list_filter = ('nombreCliente', 'correoCliente','direccionCliente') # Campos relacionados


admin.site.register(Cliente, ClienteAdmin)

