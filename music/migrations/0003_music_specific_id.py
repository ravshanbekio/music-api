# Generated by Django 4.2.7 on 2023-12-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_author_viewers_alter_album_image_alter_author_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='specific_id',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
