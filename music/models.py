from django.db import models
import datetime
from cloudinary.models import CloudinaryField
import string
import secrets

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True)
    age = models.DateField(auto_now_add=False)
    avatar = CloudinaryField(blank=True)
    listeners_per_month = models.IntegerField(default=0)
    viewers = models.PositiveBigIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Author"

    def __str__(self):
        return self.name
    
class Album(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField(blank=True)
    release_date = models.DateField() 
    author = models.ManyToManyField(Author, related_name='tracks')
    listeners_number = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Album"

    def __str__(self):
        return self.name

class Music(models.Model):
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specific_id = models.CharField(max_length=25, blank=True)
    release_date = models.DateField(auto_now_add=False)
    image = CloudinaryField(blank=True)
    duration = models.DurationField(default=datetime.timedelta(seconds=210))
    listened = models.IntegerField(default=0)
    music = CloudinaryField()

    class Meta:
        verbose_name_plural = "Music"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        if not self.specific_id:
            # Generate a random string of 25 characters (including letters and numbers)
            characters = string.ascii_letters + string.digits
            random_id = ''.join(secrets.choice(characters) for _ in range(25))

            self.specific_id = random_id

        super().save(*args, **kwargs)