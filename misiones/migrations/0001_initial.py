# Generated by Django 2.2 on 2019-09-11 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('latitud', models.CharField(blank=True, max_length=10, null=True)),
                ('longitud', models.CharField(blank=True, max_length=10, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_actualizacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Misión',
                'verbose_name_plural': 'Misiones',
                'permissions': (('add_Mision', 'Puede guardar misiones'), ('view_Mision', 'Puede ver misiones'), ('change_Mision', 'Puede actualizar misiones'), ('delete_Mision', 'Puede eliminar misiones')),
                'default_permissions': (),
            },
        ),
    ]