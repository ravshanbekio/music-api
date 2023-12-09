from rest_framework.serializers import ModelSerializer
from .models import *

class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'

class PlayedSerializer(ModelSerializer):
    class Meta:
        model = Played
        fields = '__all__'