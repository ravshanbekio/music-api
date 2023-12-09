from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.throttling import ScopedRateThrottle
from .models import Author, Album, Music
from .serializers import AuthorSerializer, AlbumSerializer, MusicSerializer

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'slug'
    allowed_methods = ['GET','POST','PUT']
    http_method_names = ['get','post','put']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'

    @action(detail=True, methods=["GET"])
    def albums(self, request, slug):
        author = Author.objects.get(slug=slug)
        get_albums = Album.objects.filter(author=author)
        serializer = AlbumSerializer(get_albums, many=True)
        return Response(serializer.data)

class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    allowed_methods = ['GET','POST','PUT']
    http_method_names = ['get','post','put']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'


class MusicViewSet(ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    lookup_field = 'specific_id'
    allowed_methods = ['GET','POST','PUT']
    http_method_names = ['get','post','put']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'

    def retrieve(self, request,pk=None, *args, **kwargs):
        queryset = Music.objects.all()
        music = get_object_or_404(queryset, pk=pk)
        music.listened += 1
        music.save()
        serializer = MusicSerializer(music)
        return Response(serializer.data)