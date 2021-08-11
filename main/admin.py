from main.models import Message
from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Usuario)
admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Evento)
admin.site.register(Astro)
admin.site.register(Estrella)
admin.site.register(Planeta)
admin.site.register(Satelite)