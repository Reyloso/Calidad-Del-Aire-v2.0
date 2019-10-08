from django.contrib import admin
from misiones.models import *

class Misiones(admin.ModelAdmin):
        # def add_view(self, request,obj, *args, **kwargs):
        #     self.fields = ('nombre','descripcion','estado',)
        #     return super(Misiones, self).add_view(*args, **kwargs)

        # def change_view(self, request,*args, **kwargs):
        #     self.fields = ('nombre','descripcion','estado',)
        #     return super(Misiones, self).change_view(*args, **kwargs)

        list_filter = ['estado','comandante']
        list_display = ['nombre','comandante','latitud','longitud','descripcion','estado','fecha_creacion','fecha_fin']
        search_fields = ['nombre','comandante']
        # inlines = [
        #     Abonos
        # ]
        class Meta:
		          model = Mision

class Mediciones(admin.ModelAdmin):

        # list_filter = ['estado']
        list_display = ['mision','data','fecha_creacion','fecha_eliminacion']
        search_fields = ['mision']

        class Meta:
		          model = Medicion



admin.site.register(Mision,Misiones)
admin.site.register(Medicion,Mediciones)