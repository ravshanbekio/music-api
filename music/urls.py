from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, AlbumViewSet, MusicViewSet

router = routers.DefaultRouter()
router.register('artist',AuthorViewSet)
router.register('album',AlbumViewSet)
router.register('music',MusicViewSet)

urlpatterns = [
    path('',include(router.urls))
]