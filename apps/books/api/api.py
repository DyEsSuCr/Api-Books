from rest_framework.viewsets import ModelViewSet
from apps.books.api.serealizers import BookSerealizer, GenderSerealizer, LenguajeSerealizer

class GenderViewSet(ModelViewSet):
  serializer_class = GenderSerealizer
  queryset = GenderSerealizer.Meta.model.objects.all()


class LengujeViewSet(ModelViewSet):
  serializer_class = LenguajeSerealizer
  queryset = LenguajeSerealizer.Meta.model.objects.all()

class BookViewSet(ModelViewSet):
  serializer_class = BookSerealizer
  queryset = BookSerealizer.Meta.model.objects.all()