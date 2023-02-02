from rest_framework.serializers import ModelSerializer
from apps.authors.api.serealizers import AuthorSerealizer
from apps.books.models import Book, Gender, Lenguaje
class GenderSerealizer(ModelSerializer):

  class Meta:
    model = Gender
    fields = '__all__'


class LenguajeSerealizer(ModelSerializer):
  
  class Meta:
    model = Lenguaje
    fields = '__all__'


class BookSerealizer(ModelSerializer):

  gender = GenderSerealizer(many=True)
  author = AuthorSerealizer(many=True)
  class Meta:
    model = Book
    fields = '__all__'