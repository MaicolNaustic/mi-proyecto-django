# Generated by Django 5.2.3 on 2025-06-30 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajadores', '0002_empresa_remove_trabajador_apellido_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
