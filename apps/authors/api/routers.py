from rest_framework.routers import DefaultRouter
from apps.authors.api.api import CountriesViewSet, AuthorViewSet

router = DefaultRouter()

router.register('countries', CountriesViewSet, 'countries')
router.register('authors', AuthorViewSet, 'authors')

urlpatterns = router.urls