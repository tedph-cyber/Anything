import uuid 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    content = models.TextField()
    section = models.ForeignKey(Section, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title