# Generated by Django 3.2.5 on 2021-08-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_astro_comment_estrella_evento_planeta_post_satelite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='profilePicUrl',
            field=models.ImageField(blank=True, upload_to='main/media/fotos_perfil'),
        ),
    ]