# Generated by Django 4.2.7 on 2023-12-08 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_hotmusic_image_alter_newmusic_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmusic',
            name='music',
        ),
        migrations.DeleteModel(
            name='HotMusic',
        ),
        migrations.DeleteModel(
            name='NewMusic',
        ),
    ]
