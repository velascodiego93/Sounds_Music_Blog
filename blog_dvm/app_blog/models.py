from django.db import models
from django import utils

# Create your models here.

class Usuario (models.Model):
    name = models.CharField (max_length=40)
    last_name = models.CharField (max_length=60)
    username = models.CharField (max_length=40, primary_key=True)
    email = models.EmailField (max_length=60)
    occupation = models.CharField(max_length=60, default='')
    workplace = models.CharField (max_length=60, default='')

    def __str__(self):
        return f'Nombre: {self.name} {self.last_name}   |   Usuario: {self.username}'


class Publicacion (models.Model):
    title = models.CharField (max_length=50, default='Missing title')
    subtitle = models.CharField (max_length=100, default='Missing subtitle')
    date_of_publication = models.DateField (default=utils.timezone.now)
    author = models.CharField (max_length=40, default='Missing author')
    post = models.CharField (max_length=2500, primary_key=True)

    def __str__ (self):
        return f'Titulo: {self.title}   |   Autor: {self.author}   |   Fecha: {self.date_of_publication}'


class Suscriptores (models.Model):
    name = models.CharField (max_length=40)
    last_name = models.CharField (max_length=60)
    email = models.EmailField (max_length=60, primary_key=True)

    def __str__(self):
        return f'Nombre: {self.name} {self.last_name}   |   E-mail: {self.email}'
