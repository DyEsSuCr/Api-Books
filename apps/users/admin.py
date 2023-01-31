from django.contrib import admin
from apps.users.models import User

# Register your models here.

class CustomUser(admin.ModelAdmin):
  list_display = ('username', 'avatar', 'created_at')
  list_editable = ('avatar', )

admin.site.register(User, CustomUser)