# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

class ContenidoPagina(models.Model):
	quienes_somos = tinymce_models.HTMLField()
	mision = tinymce_models.HTMLField()
	vision = tinymce_models.HTMLField()

	def __str__(self):
		return ('Contenido del Sitio Web')

	class Meta:
		verbose_name_plural = "Administración del Sitio Web"	


class Proyecto(models.Model):
	nombre = models.CharField(max_length=120)
	fecha_registro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre

class ImagenProyecto(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='imagenes_del_proyecto')
	imagen = models.ImageField(upload_to="proyectos/")
	imagen_thumbnail = ImageSpecField(source='imagen',
                                      processors=[ResizeToFill(190, 190)],
                                      format='JPEG',
                                      options={'quality': 100})


class Usuario(models.Model):
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	email = models.EmailField(max_length=60, unique=True)
	celular = models.CharField(max_length=10)
	fecha_registro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombres+' '+self.apellidos


class Mensaje(models.Model):
	usuario = models.ForeignKey(Usuario)
	mensaje = models.TextField()
	fecha_envio = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.mensaje[:60]



