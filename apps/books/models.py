from django.db import models

# Create your models here.

class Gender(models.Model):
  name = models.CharField('Genero', max_length=120, unique=True)

  class Meta:
    ordering = ['name']
    db_table = 'gender'
    verbose_name = 'Genero'
    verbose_name_plural = 'Generos'

  def __str__(self):
    return f'{self.name}'


class Book(models.Model):
  title = models.CharField('Titulo', max_length=120, unique=True)
  author = models.ManyToManyField("authors.Author", verbose_name="Author")
  gender = models.ManyToManyField("Gender", verbose_name="Genero")

  class Meta:
    ordering = ['title']
    db_table = 'book'
    verbose_name = 'Libro'
    verbose_name_plural = 'Libros'

  def __str__(self):
    return f'{self.title}'
  