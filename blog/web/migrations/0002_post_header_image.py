# Generated by Django 4.2.20 on 2025-03-30 12:33

from django.db import migrations
import django_resized.forms
import utils.photo_path


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[700, 220], upload_to=utils.photo_path.get_photo_path_name),
        ),
    ]
