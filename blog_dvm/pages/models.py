from django.db import models
from django import utils

# Create your models here.

class Publicacion (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField (max_length=100, default='Missing title')
    subtitle = models.CharField (max_length=150, default='Missing subtitle')
    date_of_publication = models.DateField (default=utils.timezone.now)
    author = models.CharField (max_length=150, default='Missing author')
    post = models.CharField (max_length=15000)
    image = models.ImageField (upload_to = 'posts_img', null = True, blank = True)

    def __str__ (self):
        return f'Titulo: {self.title}   |   Autor: {self.author}   |   Fecha: {self.date_of_publication}'



