from django import forms
from django.core.validators import RegexValidator

CONTRASEÑA_REGEX = RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}',
                                  'Escriba una contraseña entre 8 y 15 caracteres, al menos una letra minúscula, otra mayúscula, un número y un carácter especial.')


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="Apellidos",  widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    email = forms.EmailField(label="E-mail",  widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'error_message':'Introduzca un e-mail válido'}))
    password = forms.CharField(validators=[CONTRASEÑA_REGEX], label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    address = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
    city = forms.CharField(label="Ciudad", widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class EditProfile(forms.Form):
    profilePhoto = forms.ImageField(label="Foto de perfil", required=False)
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="Apellidos",  widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    email = forms.EmailField(label="E-mail",  widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'error_message':'Introduzca un e-mail válido'}))
    address = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
    city = forms.CharField(label="Ciudad", widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))

class CreatePostForm(forms.Form):
    title = forms.CharField(label="Título", widget=forms.TextInput(attrs={'placeholder': 'Título'}))
    photo = forms.ImageField(label="Foto de la publicación", required=True)

class CreateCommentForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escribe tu comentario'}))

class CreateEventoForm(forms.Form):
    title = forms.CharField(label="Título", widget=forms.TextInput(attrs={'placeholder': 'Título'}))
    description = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'placeholder': 'Descripción'}))
    photo = forms.ImageField(label="Foto de la publicación", required=True)

class SearchInfo(forms.Form):
    info = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Buscar'}))
