from django.db import models
from login.models import User


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    #tags = models.ManyToManyField(Tag, verbose_name="question tags")
    desc = models.CharField(max_length=300)
    popularity = models.IntegerField()
    title = models.CharField(max_length=100)
    ans_cnt = models.IntegerField()
    user = models.ForeignKey(User)


class Answer(models.Model):
    pass