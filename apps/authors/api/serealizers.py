from rest_framework.serializers import ModelSerializer
from apps.authors.models import Countries, Author
class CountriesSerealizer(ModelSerializer):

  class Meta:
    model = Countries
    fields = '__all__'


class AuthorSerealizer(ModelSerializer):

  nacionality = CountriesSerealizer()
  class Meta:
    model = Author
    fields = '__all__'