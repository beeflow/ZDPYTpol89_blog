# Generated by Django 4.2.20 on 2025-04-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
