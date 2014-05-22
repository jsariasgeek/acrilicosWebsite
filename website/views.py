# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from website.models import *
from website.forms import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.db import IntegrityError

# Create your views here.

def home(request):
	form = FormularioContacto()
	proyectoDesorder = Proyecto.objects.all()
	proyecto = proyectoDesorder.order_by('-fecha_registro')
	contenido = ContenidoPagina.objects.all()
	return render_to_response('index.html', dict(form = form, proyecto=proyecto, contenido=contenido), context_instance=RequestContext(request))


def contacto(request):
	if request.method == 'POST': # Si el formulario es enviado
		form = FormularioContacto(request.POST)		
		if form.is_valid(): # Si es válido se procesan los datos
			nombres = form.cleaned_data['nombre']
			apellidos = form.cleaned_data['apellidos']
			email = form.cleaned_data['email']
			celular = form.cleaned_data['celular']
			mensajeUsuario = form.cleaned_data['mensaje']					
			subject = 'Te han dejado un mensaje en la web'
			message = nombres + ' ' + apellidos + ' con el email ' + email + ' y celular ' + celular + ' te ha dejado el siguiente mensaje en la web:  ' + mensajeUsuario
			# Enviamos el mensaje
			mail = EmailMessage(subject, message, to=['jsarias1993@gmail.com'])
			mail.send()

			# Guardamos los datos del usuario
			userMessage = Usuario()
			userMessage.nombres = form.cleaned_data['nombre']
			userMessage.apellidos = form.cleaned_data['apellidos']
			userMessage.email = form.cleaned_data['email']
			userMessage.celular = form.cleaned_data['celular']

			
			# Guardamos el Mensaje

			# Guardamos el usuario
			try:
				userMessage.save()
				userMessage.mensaje_set.create(mensaje=mensajeUsuario)
				return redirect('/mensajeenviado/')

			except IntegrityError:
				# confirmamos el envío del mensaje			
				UserHistorico = Usuario.objects.get(email=email)
				messageUser = Mensaje()
				messageUser.usuario = UserHistorico
				messageUser.mensaje = mensajeUsuario
				messageUser.save()
				return redirect('/mensajeenviado/')
			
	else:
		form = FormularioContacto() # An unbound form

	return render_to_response('index.html', dict(form=form), context_instance=RequestContext(request))

def paginaProyecto(request, pk):
	proyecto = Proyecto.objects.get(pk=int(pk))
	return render_to_response('paginaProyecto.html', dict(proyecto=proyecto, usuario=request.user))



def gracias(request):
	return render_to_response('confirmacion.html')