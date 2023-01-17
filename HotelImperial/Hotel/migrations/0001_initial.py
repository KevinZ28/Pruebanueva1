# Generated by Django 4.0.5 on 2022-07-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='about', verbose_name='Imagen')),
                ('image_security', models.ImageField(upload_to='about', verbose_name='Imagen de Seguridad')),
                ('description_security', models.TextField(verbose_name='Descripcion de Seguridad')),
                ('image_price', models.ImageField(upload_to='about', verbose_name='Imagen de Precio')),
                ('description_price', models.TextField(verbose_name='Descripcion de Precio')),
                ('image_availability', models.ImageField(upload_to='about', verbose_name='Imagen de Disponibilidad')),
                ('description_availability', models.TextField(verbose_name='Descripcion de Disponibilidad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Nosotro',
                'verbose_name_plural': 'Nosotros',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('image', models.ImageField(upload_to='blog', verbose_name='Imagen')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('image', models.ImageField(upload_to='rooms', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['-created'],
            },
        ),
    ]
