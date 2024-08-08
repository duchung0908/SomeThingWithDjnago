from django import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class UploadedFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)
    

    def clean(self):
        if self.file.size > 2*1024*1024:
            raise ValueError("dddddd")
        return True


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()