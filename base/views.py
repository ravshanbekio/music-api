from rest_framework.viewsets import ModelViewSet
from .models import Favorites, Played, HotMusic, NewMusic
from .serializers import FavoriteSerializer, PlayedSerializer, HotMusicSerializer, NewMusicSerializer

class FavoriteViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer
    #lookup_field = 'slug'
    allowed_methods = ['GET','POST','PUT']
    http_method_names = ['get','post','put']

class PlayedViewSet(ModelViewSet):
    queryset = Played.objects.all()
    serializer_class = PlayedSerializer
    #lookup_field = 'slug'
    allowed_methods = ['GET','POST','PUT']
    http_method_names = ['get','post','put']