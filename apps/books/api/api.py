from rest_framework.viewsets import ModelViewSet
from apps.books.api.serealizers import BookSerealizer, GenderSerealizer

class GenderViewSet(ModelViewSet):
  serializer_class = GenderSerealizer
  queryset = GenderSerealizer.Meta.model.objects.all()

class BookViewSet(ModelViewSet):
  serializer_class = BookSerealizer
  queryset = BookSerealizer.Meta.model.objects.all()