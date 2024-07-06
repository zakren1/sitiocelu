from django import forms
from .models import Celular, CustomUser, Pedido
from .enumeraciones import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'rut', 'nombre', 'apellido', 'username', 'telefono','region','comuna','direccion','num_departamento', 'password1','password2']

class CustomUserUpdateForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('email', 'rut', 'nombre', 'apellido', 'username', 'is_active', 'telefono', 'region', 'comuna', 'direccion', 'num_departamento',)
        widgets = {
            'rut': forms.TextInput(attrs={'readonly': True}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

'''class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rut','nombre','apellido','username','correo','password']

class UpdateUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','username','correo','telefono','region','comuna','direccion','num_departamento']'''

class CelularForm(forms.ModelForm):
    
    class Meta:
        model = Celular
        fields = ['modelo','marca','precio','especificaciones','foto']

class UpdateCelularForm(forms.ModelForm):
    
    class Meta:
        model = Celular
        fields = ['modelo','marca','precio','especificaciones','foto']
        
class ActualizarEstadoPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']

    