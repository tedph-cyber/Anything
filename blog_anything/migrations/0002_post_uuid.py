# Generated by Django 5.1.2 on 2024-11-16 00:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_anything', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]