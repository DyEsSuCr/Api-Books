from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from apps.books.api.serealizers import BookSerealizer, GenderSerealizer, LenguajeSerealizer

# Create your views here.

class GenderViewSet(ModelViewSet):
  serializer_class = GenderSerealizer

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(state = True)
    return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()


  def list(self, request):
    gender_serealizer = self.get_serializer(self.get_queryset(), many = True)
    return Response(gender_serealizer.data, status=status.HTTP_200_OK)


  def create(self, request):
    serealizer = self.get_serializer(data = request.data)

    if serealizer.is_valid():
      serealizer.save()
      return Response({'menssaje': 'Creado con exito!'}, status=status.HTTP_201_CREATED)
    return Response(serealizer.errors, status=status.HTTP_400_BAD_REQUEST)


  def update(self, request, pk=None):
    if self.get_queryset(pk):
      gender_serealizer = self.get_serializer(self.get_queryset(pk), data = request.data)
      
      if gender_serealizer.is_valid():
        gender_serealizer.save()
        return Response({'messaje': 'Actualizado con exito', 'data': gender_serealizer.data}, status=status.HTTP_200_OK)
      return Response(gender_serealizer.errors, status=status.HTTP_400_BAD_REQUEST)


  def destroy(self, request, pk=None):
    gender = self.get_queryset().filter(id=pk).first()

    if gender:
      gender.state = False
      gender.save()
      return Response({'messaje': 'Eliminacion exitosa!'}, status=status.HTTP_200_OK)
    return Response({'error': 'Error'})


class LengujeViewSet(ModelViewSet):
  serializer_class = LenguajeSerealizer
  queryset = LenguajeSerealizer.Meta.model.objects.all()


class BookViewSet(ModelViewSet):
  serializer_class = BookSerealizer
  queryset = BookSerealizer.Meta.model.objects.all()