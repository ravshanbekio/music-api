from django.db import models
from music.models import Music
from accounts.models import User
from cloudinary.models import CloudinaryField

class Favorites(models.Model):
    music = models.ManyToManyField(Music)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Favorites"

    def __str__(self):
        return self.user.full_name
    
class Played(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Recently played"

    def __str__(self):
        return self.user.username