from django.contrib import admin
from apps.authors.models import Countries, Author

# Register your models here.

admin.site.register(Countries)
admin.site.register(Author)