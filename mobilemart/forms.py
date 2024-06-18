
from django import forms
from .models import Usuario
from .enumeraciones import *




class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rut','nombre','apellido','username','correo','password']

class UpdateUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','username','correo','telefono','region','comuna','num_departamento']

    