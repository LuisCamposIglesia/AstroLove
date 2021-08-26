from main.filters import ChatFilter, EventFilter
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
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/posts/")

@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect("/posts/")

@login_required
def chats(request):
    usuarios = Usuario.objects.all()
    chatFilter = ChatFilter(
                request.GET, queryset=usuarios)
    usuarios = chatFilter.qs  
    return render(request, 'chats.html', {'usuarios':usuarios, 'chatFilter':chatFilter, 'user':request.user})

@login_required
def room(request, user_id, my_id):
    usuarios = Usuario.objects.all()
    chatFilter = ChatFilter(
                request.GET, queryset=usuarios)
    usuarios = chatFilter.qs
    usuario = Usuario.objects.get(user__id=user_id)
    i_usuario =  Usuario.objects.get(user__id=my_id)
    room_id = ""
    author = i_usuario.nombreCompleto
    if user_id > my_id:
        room_id = str(user_id) + str(my_id)
    else:
        room_id = str(my_id) + str(user_id)
    return render(request, 'chats.html', {'room_id':room_id, 'chatFilter':chatFilter, 'usuario_chat':usuario,'usuarios':usuarios, 'i_usuario':i_usuario
    , "author": author})


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
    eventos = Evento.objects.all().order_by('-date')
    lengths = []
    eventFilter = EventFilter(
                request.GET, queryset=eventos)
    eventos = eventFilter.qs

    for evento in eventos:
     lengths.append(len(evento.apuntados.all()))   
    items = zip(eventos, lengths)
    return render(request, 'eventos.html', {'items':items, 'eventFilter': eventFilter})  
    



@login_required
def create_evento(request):
    if request.method == "POST":
        form = CreateEventoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            photo = form.cleaned_data['photo']
            date = datetime.now()
            evento = Evento(title=title, description= description, photo=photo, date = date)
            evento.save()   
            return redirect("/eventos")
        else:
            return render(request, 'createEvento.html', {'form': form})
    form = CreateEventoForm()
    return render(request, 'createEvento.html',{'form': form})






@login_required
def delete_evento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect("/eventos/")

@login_required
def show_evento(request, id):
    # AQUI NO TE HACE FALTA UN FORMULARIO, YA QUE EXCLUSIVAMENTE VAS A MOSTRAR EL EVENTO
    evento = Evento.objects.get(id=id)
    apuntados = evento.apuntados.all()
    current_user = Usuario.objects.get(user=request.user)
    return render(request, 'showEvento.html', {'evento': evento, 'apuntados':apuntados, 'current_user':current_user })

@login_required
def new_apuntado(request, evento_id, user_id):
    evento = Evento.objects.get(id=evento_id)
    apuntados = evento.apuntados.all()
    usuario = Usuario.objects.get(id=user_id)
    if usuario not in apuntados:
        apuntados |=  Usuario.objects.filter(id=user_id)
        evento.apuntados.set( apuntados)
        evento.save()
    return redirect("/eventos/show/"+str(evento.id))


@login_required
def logout(request):
    do_logout(request)
    response = redirect('/')
    return response
