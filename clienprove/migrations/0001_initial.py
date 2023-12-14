# Generated by Django 4.2.6 on 2023-12-14 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='nombre', max_length=64)),
                ('Apellido', models.CharField(default='Apellido', max_length=64)),
                ('telefono', models.CharField(default='Telefono', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='nombre', max_length=64)),
                ('Apellido', models.CharField(default='Apellido', max_length=64)),
                ('telefono', models.CharField(default='Telefono', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_1', models.TextField(default='1')),
                ('campo_2', models.TextField(default='1')),
                ('campo_3', models.TextField(default='1')),
                ('campo_4', models.TextField(default='1')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clienprove.cliente')),
            ],
        ),
    ]