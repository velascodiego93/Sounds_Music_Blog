from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suscriptores (models.Model):
    name = models.CharField (max_length=40)
    last_name = models.CharField (max_length=60)
    email = models.EmailField (max_length=60, primary_key=True)

    def __str__(self):
        return f'Nombre: {self.name} {self.last_name}   |   E-mail: {self.email}'


class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField (upload_to = 'avatars', null = True, blank = True)


class UserExtraInformation (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField (max_length=400)
    web_page = models.CharField (max_length=150)

    def __str__ (self):

        username = User.objects.filter(id = self.user_id)[0].username
        return f'{username}  |  description: {self.description}  |  web page: {self.web_page}'
    
