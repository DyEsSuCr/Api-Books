from rest_framework.viewsets import ModelViewSet
from apps.authors.api.serealizers import CountriesSerealizer, AuthorSerealizer

class CountriesViewSet(ModelViewSet):
  serializer_class = CountriesSerealizer
  queryset = CountriesSerealizer.Meta.model.objects.all()

class AuthorViewSet(ModelViewSet):
  serializer_class = AuthorSerealizer
  queryset = AuthorSerealizer.Meta.model.objects.all()