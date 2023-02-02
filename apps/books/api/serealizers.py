from rest_framework.serializers import ModelSerializer
from apps.authors.api.serealizers import AuthorSerealizer
from apps.books.models import Book, Gender
class GenderSerealizer(ModelSerializer):

  class Meta:
    model = Gender
    fields = ('id', 'name')


class BookSerealizer(ModelSerializer):

  gender = GenderSerealizer(many=True)
  author = AuthorSerealizer(many=True)
  class Meta:
    model = Book
    fields = '__all__'