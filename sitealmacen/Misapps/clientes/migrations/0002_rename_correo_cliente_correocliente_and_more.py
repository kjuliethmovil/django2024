# Generated by Django 5.1.1 on 2024-09-26 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='correo',
            new_name='correoCliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='direccion',
            new_name='direccionCliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='nombreCliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefonoC',
            new_name='telefonoCliente',
        ),
    ]
