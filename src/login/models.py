from django.db import models


class User(models.Model):
    img = models.FilePathField()
    login = models.CharField(max_length=30, primary_key=True)
    password = models.IntegerField()
