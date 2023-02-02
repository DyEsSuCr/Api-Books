from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  avatar = models.ImageField('Avatar', default='avatars/default-avatar.png', upload_to='avatars', blank=True, null=True)
  created_at = models.DateTimeField('Fecha de creación', auto_now=True, auto_now_add=False)

  class Meta:
    ordering = ["created_at"]
    db_table = 'auth_user'
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'

  @property
  def get_avatar(self):
    if self.avatar:
      return self.avatar.url