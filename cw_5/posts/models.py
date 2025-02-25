from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.FileField(upload_to='post_pictures/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)  # Создайте модель Thread

    def _str_(self):
        return self.title

class Thread(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name