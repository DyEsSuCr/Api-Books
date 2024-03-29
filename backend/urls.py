from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('users/', include('apps.users.api.routers')),
    path('authors/', include('apps.authors.api.routers')),
    path('books/', include('apps.books.api.routers')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]