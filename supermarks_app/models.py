from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(auto_now=True)


class BookMark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='bookmarks')


class MarkUser(models.Model):
    user = models.OneToOneField(User)
    bookmarks = models.ManyToManyField(BookMark, related_name='bookmarks')

