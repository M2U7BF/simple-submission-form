from turtle import title
from django.db import models

# Create your models here.
class PostModel(models.Model):
    # モデルではfieldをセット
    title = models.CharField(max_length= 50)
    memo = models.TextField()

    def __str__(self):
        return self.title