from rest_framework.routers import DefaultRouter
from apps.books.api.api import BookViewSet, GenderViewSet, LengujeViewSet

router = DefaultRouter()

router.register('genders', GenderViewSet, 'genders')
router.register('books', BookViewSet, 'books')
router.register('lenguajes', LengujeViewSet, 'lenguajes')

urlpatterns = router.urls