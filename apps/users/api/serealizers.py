from rest_framework.serializers import ModelSerializer
from apps.users.models import User

class UserSerealLizer(ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'avatar', 'is_active')