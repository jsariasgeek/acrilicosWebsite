from django import forms

class FormularioContacto(forms.Form):
	nombre =forms.CharField(max_length=60)
	apellidos = forms.CharField(max_length=60)
	email = forms.EmailField(max_length=60)
	celular = forms.CharField(max_length=60)	
	mensaje = forms.CharField(widget=forms.Textarea)
	

