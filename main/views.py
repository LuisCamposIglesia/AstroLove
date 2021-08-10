from django.core.checks.messages import Error
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as do_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as do_logout



from .forms import *
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            try:
                user = User(username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password);
                user.save()
                usuario = Usuario(address=address, city=city, profilePicUrl="",photo="", isDeleted = False,
                isAccountNonExpired=False,isEnabled=True,isPro= False, user=user)
                usuario.save()
                usuario_login = authenticate(username=username, password=password)
                do_login(request,usuario_login)
                return redirect("/home")
            except Exception as e:
                print(e)
                er_msg = "El nombre de usuario ya está ocupado, por favor cámbielo."
                return render(request, "registro.html", {'form': form, 'er_msg': er_msg})
        else:
            return render(request, 'registro.html', {'form': form})
    form = UserRegisterForm()
    return render(request, "registro.html", {'form': form})

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                do_login(request, usuario)
                return redirect("/home")
            else:
                er_msg = "Error al introducir los datos. No coincide ningún usuario con los datos introducidos."
                return render(request, "login.html", {'form': form, 'er_msg': er_msg})
        else:
            return render(request, 'login.html', {'form': form})
    form = UserLoginForm()
    return render(request, 'registro.html',{'form': form})

@login_required
def home(request):
    usuario = request.user
    return render(request, 'home.html',{'usuario':usuario})

@login_required
def informacion(request):
    return render(request, 'informacion.html')

@login_required
def posts(request):
    return render(request, 'posts.html')

@login_required
def chats(request):
    return render(request, 'chats.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def eventos(request):
    return render(request, 'eventos.html')

@login_required
def logout(request):
    do_logout(request)
    response = redirect('/')
    return response
