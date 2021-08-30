"""AstroSocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login),
    path('registro/', views.registro),
    path('home/', views.home),
    path('perfil/', views.perfil),
    path('posts/', views.posts),
    path('chats/', views.chats),
    path('chats/<int:user_id>/<int:my_id>/', views.room),
    path('eventos/', views.eventos),
    path('eventos/create/', views.create_evento),
    path('eventos/delete/<int:id>/', views.delete_evento),
    path('eventos/show/<int:id>/', views.show_evento),
    path('eventos/new_user/<int:evento_id>/<int:user_id>/', views.new_apuntado),
    path('informacion/', views.informacion),
    path('inicio/informacion/', views.informacion2),
    path('logout/', views.logout),
    path('perfil/update/', views.modificarPerfil),
    path('posts/create/', views.create_post),
    path('posts/show/<int:id>/', views.show_post),
    path('posts/<int:id>/like/', views.like_post),
    path('posts/<int:id>/dislike/', views.dislike_post),
    path('posts/delete/<int:id>/', views.delete_post),
    path('comment/delete/<int:id>/', views.delete_comment),
    path('userlist/', views.userlist),
    path('userlist/delete/<int:id>/', views.delete_user),




]
