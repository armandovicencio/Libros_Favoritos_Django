# Generated by Django 4.0.2 on 2022-03-04 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acceso', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='acceso.usuario')),
                ('favorito', models.ManyToManyField(related_name='favoritos', to='acceso.Usuario')),
            ],
        ),
    ]
