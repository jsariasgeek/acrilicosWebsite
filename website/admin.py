from django.contrib import admin
from website.models import *

# Register your models here.

class ImagenProyectoInline(admin.StackedInline):
	model = ImagenProyecto
	extra = 4

class ProyectoAdmin(admin.ModelAdmin):	
    fieldsets = [
        (None,{'fields': ['nombre']}),  
                             
    ]
    inlines = [ImagenProyectoInline]
    list_display = ('nombre', 'fecha_registro')

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nombres', 'apellidos', 'email', 'celular', 'fecha_registro']


class MensajeAdmin(admin.ModelAdmin):
	list_display = ['usuario', 'mensaje', 'fecha_envio']


class ContenidoPaginaAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,{'fields': ['quienes_somos']}),  
        (None,{'fields': ['mision']}),
        (None,{'fields': ['vision']}),         
                             
    ]

	


admin.site.register(Proyecto, ProyectoAdmin,)
admin.site.register(Usuario, UsuarioAdmin,)
admin.site.register(Mensaje, MensajeAdmin,)
admin.site.register(ContenidoPagina, ContenidoPaginaAdmin)


