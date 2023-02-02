from django.db import models

# Create your models here.

class Countries(models.Model):
  name = models.CharField('Nacionalidad', max_length=120, unique=True)

  class Meta:
    ordering = ['name']
    db_table = 'countries'
    verbose_name = 'Pais'
    verbose_name_plural = 'Paises'

  def __str__(self):
    return f'{self.name}'


class Author(models.Model):
  first_name = models.CharField('Nombres', max_length=120)
  last_name = models.CharField('Apellidos', max_length=120)
  photo = models.ImageField('Foto', upload_to='authors', blank=True, null=True)
  birth = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False)
  nacionality = models.OneToOneField("Countries", verbose_name="nacionalidad", on_delete=models.CASCADE)


  class Meta:
    ordering = ['first_name']
    db_table = 'author'
    verbose_name = 'Autor'
    verbose_name_plural = 'Autores'

  def __str__(self):
    return f'{self.first_name} - {self.last_name}'

  @property
  def get_photo(self):
    if self.photo:
      return self.photo.url