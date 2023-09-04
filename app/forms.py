from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    direccion = forms.CharField(max_length=100, required=True)
    nombre = forms.CharField(label="Nombre/s", max_length=50, required=False)
    apellido = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'direccion', 'nombre', 'apellido']

class EditarUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    nombre = forms.CharField(label="Nombre/s", max_length=50, required=False)
    apellido = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email','password1','password2','nombre','apellido']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

