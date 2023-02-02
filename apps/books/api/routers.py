from rest_framework.routers import DefaultRouter
from apps.books.api.api import BookViewSet, GenderViewSet

router = DefaultRouter()

router.register('genders', GenderViewSet, 'genders')
router.register('books', BookViewSet, 'books')

urlpatterns = router.urls