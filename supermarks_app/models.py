from django.db import models
from django.contrib.auth.models import User


class BookMarks(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tags, related_name='bookmarks')


class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(auto_now=True)


class MarkUsers(models.Model):
    user = models.OneToOneField(User)
    bookmarks = models.ManyToManyField(BookMarks, related_name='bookmarks')


