from django.contrib import admin
from apps.books.models import Book, Gender, Lenguaje

# Register your models here.

admin.site.register(Book)
admin.site.register(Gender)
admin.site.register(Lenguaje)
