from django.core.checks.messages import Error
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as do_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as do_logout
from datetime import datetime    



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
    posts = Post.objects.all().order_by('-date')
    likes = []
    for post in posts:
        likes.append(len(Like.objects.filter(post=post)))
    items = zip(posts, likes)
    return render(request, 'posts.html', {'items':items})

@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            photo = form.cleaned_data['photo']
            creator = Usuario.objects.get(user=request.user)
            date = datetime.now()
            post = Post(title=title, photo=photo, creator = creator, date = date)
            post.save()
            return redirect("/posts")
        else:
            return render(request, 'createPost.html', {'form': form})
    form = CreatePostForm()
    return render(request, 'createPost.html',{'form': form})

@login_required
def show_post(request, id):
    post = Post.objects.get(id=id)
    likes = len(Like.objects.filter(post=post))
    comments = Comment.objects.filter(post=post).order_by('-time')
    if request.method == "POST":
        form = CreateCommentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data['content']
            creator = Usuario.objects.get(user=request.user)
            date = datetime.now()
            comment = Comment(content=content, time=date, creator = creator, post = post)
            comment.save()
            return redirect("/posts/show/" + str(post.id)+"/")
        else:
            return render(request, 'showPost.html', {'post':post, 'likes':likes, 'comments':comments, 'form':form})
    form = CreateCommentForm()
    return render(request, 'showPost.html', {'post':post, 'likes':likes, 'comments':comments, 'form':form})

@login_required
def chats(request):
    return render(request, 'chats.html')

@login_required
def perfil(request):
    usuario = Usuario.objects.get(user=request.user)
    return render(request, 'perfil.html', {"usuario":usuario})

@login_required
def modificarPerfil(request): 
    usuario = Usuario.objects.get(user = request.user)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            profilePhoto = form.cleaned_data['profilePhoto']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            usuario = Usuario.objects.get(user=request.user)
            if profilePhoto:
                usuario.profilePicUrl = profilePhoto
            
            usuario.email = email
            usuario.address = address
            usuario.city = city
            usuario.user.first_name = first_name
            usuario.user.last_name = last_name
            usuario.save()
            return redirect('/perfil')
        else:
            valores = [usuario.profilePicUrl ,usuario.user.first_name, usuario.user.last_name, usuario.user.email, usuario.address, usuario.city]
            items = zip(form, valores)
            return render(request, 'perfil.html', {'form': form, 'items': items, 'usuario':usuario})
    form = EditProfile()
    valores = [usuario.profilePicUrl,usuario.user.first_name, usuario.user.last_name, usuario.user.email, usuario.address, usuario.city]
    items = zip(form, valores)
    return render(request, 'perfil.html', {'form': form, 'items': items, 'usuario':usuario})
    


@login_required
def eventos(request):
    return render(request, 'eventos.html')

@login_required
def logout(request):
    do_logout(request)
    response = redirect('/')
    return response
