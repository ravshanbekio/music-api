# Generated by Django 4.2.7 on 2023-12-08 12:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_music_specific_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
