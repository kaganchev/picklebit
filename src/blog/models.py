from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True, auto_now=False)
    modify_date = models.DateTimeField('date published')
    text = models.TextField()

    def __str__(self):
        return self.title
    