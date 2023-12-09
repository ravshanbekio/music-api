from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import APIException
from .models import *

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    # def validate_avatar(self, avatar):
    #     if avatar[-1: -5] != ".png" or avatar[-1: -5] != ".jpg":
    #         raise APIException("Image should be png or jpg!")
    #     return avatar

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    # def validate_image(self, image):
    #     if image[-1: -5] != ".png" or image[-1: -5] != ".jpg":
    #         raise APIException("Image should be PNG or JPG!")
    #     return image

class MusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

    # def validate_image(self, image):
    #     if image[-1: -5] != ".png" or image[-1: -5] != ".jpg":
    #         raise APIException("Image should be png or jpg!")
    #     return image
    
    def validate_duration(self, duration):
        if duration <= datetime.timedelta(seconds=60):
            raise APIException("Duration of music must be longer!")
        return duration