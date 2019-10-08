from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
import inspect, os

# Create your models here.
class Mision(models.Model):
    nombre = models.CharField(max_length=50,blank=False, null=False)
    comandante = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    latitud = models.CharField(max_length=10,blank=True, null=True)
    longitud = models.CharField(max_length=10,blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.BooleanField(null=False, default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Misión"
        verbose_name_plural = "Misiones"
        default_permissions = ()
        permissions = (
            ("add_Mision", "Puede guardar misiones"),
            ("view_Mision", "Puede ver misiones"),
            ("change_Mision", "Puede actualizar misiones"),
            ("delete_Mision", "Puede eliminar misiones"),
        )

    def __str__(self):
        return str(self.nombre)

@receiver(pre_save, sender=Mision)
def save_mision(sender, instance, **kwargs):
    if instance.estado == True:
        mision = Mision.objects.filter(estado=True).update(estado=False,fecha_fin=timezone.now())
    
class Medicion(models.Model):
    mision = models.ForeignKey(Mision, related_name='mediciones', on_delete=models.PROTECT, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Medición"
        verbose_name_plural = "Mediciones"
        default_permissions = ()
        permissions = (
            ("add_Medicion", "Puede guardar mediciones"),
            ("view_Medicion", "Puede ver mediciones"),
            ("change_Medicion", "Puede actualizar mediciones"),
            ("delete_Medicion", "Puede eliminar mediciones"),
        )

    def __str__(self):
        return str(self.mision)

@receiver(pre_save, sender=Medicion)
def save_medicion(sender, instance, **kwargs):
    mision = Mision.objects.get(estado=True)
    instance.mision = mision