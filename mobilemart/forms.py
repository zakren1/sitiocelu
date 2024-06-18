from django import forms
from .models import Usuario, Celular
from .enumeraciones import *




class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rut','nombre','apellido','username','correo','password']

class UpdateUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','username','correo','telefono','region','comuna','direccion','num_departamento']

class CelularForm(forms.ModelForm):
    
    class Meta:
        model = Celular
        fields = ['modelo','marca','precio','especificaciones','foto']

class UpdateCelularForm(forms.ModelForm):
    
    class Meta:
        model = Celular
        fields = ['modelo','marca','precio','especificaciones','foto']

    