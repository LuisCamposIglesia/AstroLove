from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    isDeleted = models.BooleanField()
    profilePicUrl = models.CharField(max_length=250)
    photo = models.CharField(max_length=550)
    isAccountNonExpired = models.BooleanField(default=False)
    isEnabled = models.BooleanField(default=False)
    isPro = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.username + "," + self.user.first_name + " " + self.user.last_name
    def nombreCompleto(self):
        return self.user.first_name + " " + self.user.last_name

class Message(models.Model):
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    seen = models.BooleanField(default=False)
    time = models.DateTimeField()
    fromUser = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='fromUser')
    toUser = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='toUser')
    def __str__(self):
        return self.fromUser.user.username + "->" + self.self.toUser.user.username + "( "+self.subject+ " )"

class Evento(models.Model):
    title = models.CharField(max_length=30)
    date =  models.DateTimeField()
    description = models.CharField(max_length=250)
    #apuntados = models.userField()
    photo = models.CharField(max_length=550)

class Post(models.Model):
    date =  models.DateTimeField()
    title = models.CharField(max_length=30)
    photo = models.CharField(max_length=550)
    like = models.IntegerField()
    creator = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=550)
    time = models.DateTimeField()
    creator = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

ASTROTYPE = (
        ('Str', 'Estrella'),
        ('Plt', 'Planeta'),
        ('Sat', 'Satelite'),
        ('Com', 'cometa'),
        ('Ast', 'Asteroide'),
        ('Exo', 'Exoplaneta'),
        ('Glx', 'Galaxia'),
        ('Cum', 'Cumulo'),
        ('Scu', 'SuperCumulo'),

    )

   

class Astro(models.Model):
    photo = models.CharField(max_length=550)
    name = models.CharField(max_length=30)
    IsInSolarSystem = models.BooleanField(default=True)
    masa = models.IntegerField()
    distancia = models.IntegerField()
    radio = models.IntegerField()
    description = models.CharField(max_length=550)
    composicion = models.CharField(max_length=550)
    astroTypes = models.TextField(max_length=3, blank=True, null=True, choices=ASTROTYPE) 


STARTYPE = (
        ('Hip', 'Hipergigante'),
        ('Spl', 'Supergigante luminosa'),
        ('Spg', 'Supergigante'),
        ('Gig', 'Gigante'),
        ('Sug', 'Sub-gigantes'),
        ('Enn', 'Enanas'),
        ('Sue', 'Sub-enanas'),
        ('Enb', 'Enanas blancas'),
    )

class Estrella (models.Model):
    astro = models.ForeignKey(Astro, on_delete=models.CASCADE,related_name='astro')
    starType = models.TextField(max_length=3, blank=True, null=True, choices=STARTYPE) 


PLANETYPE = (
        ('Roc', 'Rocoso'),
        ('Gas', 'Gaseoso'),
        ('Nep', 'Neptuniano'),
        ('Pel', 'Planeta enano'),
    )

class Planeta (models.Model):
    habitable = models.BooleanField(default=False)
    numSatelites = models.IntegerField()
    planetType = models.TextField(max_length=3, blank=True, null=True, choices=PLANETYPE) 
    astro = models.ForeignKey(Astro, on_delete=models.CASCADE)

class Satelite (models.Model):
    habitable = models.BooleanField(default=False)
    astro = models.ForeignKey(Astro, on_delete=models.CASCADE)


    

  

