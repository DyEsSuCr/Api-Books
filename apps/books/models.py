from django.db import models
from apps.base.models import BaseModel

# Create your models here.

class Gender(BaseModel):
  name = models.CharField('Genero', max_length=120, unique=True)

  class Meta:
    ordering = ['name']
    db_table = 'gender'
    verbose_name = 'Genero'
    verbose_name_plural = 'Generos'

  def __str__(self):
    return f'{self.name}'


class Lenguaje(BaseModel):

  initial = models.CharField('Lenjuage', max_length=6, unique=True)

  class Meta:
    ordering = ['initial']
    db_table = 'lenguaje'
    verbose_name = 'Lenguaje'
    verbose_name_plural = 'Lenguajes'

  def __str__(self):
    return f'{self.initial}'


class Book(BaseModel):
  title = models.CharField('Titulo', max_length=120, unique=True)
  subtitle = models.CharField('Subtitulo', max_length=120, unique=True, null=True, blank=True)
  front_page = models.ImageField('Portada', upload_to='frontpage', null=True, blank=True)
  pages = models.IntegerField(null=True, blank=True)
  publicher_date = models.DateField('Fecha de publicacion', auto_now=False, auto_now_add=False)
  author = models.ManyToManyField("authors.Author", verbose_name="Author")
  lenguaje = models.ManyToManyField('Lenguaje', verbose_name='Lenguaje')
  gender = models.ManyToManyField("Gender", verbose_name="Genero")

  class Meta:
    ordering = ['title']
    db_table = 'book'
    verbose_name = 'Libro'
    verbose_name_plural = 'Libros'

  def __str__(self):
    return f'{self.title}'

  @property
  def get_front_page(self):
    if self.front_page:
      return self.front_page.url
  