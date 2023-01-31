from rest_framework.viewsets import ModelViewSet
from apps.users.api.serealizers import UserSerealLizer

class UserViewSet(ModelViewSet):
  serializer_class = UserSerealLizer
  queryset = UserSerealLizer.Meta.model.objects.all()