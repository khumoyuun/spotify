from rest_framework import routers

from . import views
from .views import SongViewSet, AlbumViewSet, ArtistViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)
router.register('artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
