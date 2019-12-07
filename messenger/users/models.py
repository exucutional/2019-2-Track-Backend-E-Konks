from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    bio = models.TextField(verbose_name='Биография', null=True, default='', blank=True)
    contacts = models.ManyToManyField('User', blank=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
