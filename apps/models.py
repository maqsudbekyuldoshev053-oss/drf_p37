from django.db import models
from django.db.models import Model, TextField, CharField, IntegerField, EmailField, ForeignKey, CASCADE, URLField, \
    BooleanField


class Post(Model):
    userId = ForeignKey('apps.User', CASCADE, related_name='posts')
    title = CharField(max_length=255)
    body = TextField()


class Comments(Model):
    postId = ForeignKey('apps.Post', CASCADE, related_name='comments')
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    body = TextField()


class Album(Model):
    userId = ForeignKey('apps.User', CASCADE, related_name='albums')
    title = CharField(max_length=255)


class Photo(Model):
    albumId = ForeignKey('apps.Album', CASCADE, related_name='photos')
    title = CharField(max_length=255)
    url = URLField(max_length=255)
    thumbnailUrl = URLField(max_length=255)


class Todo(Model):
    userId = ForeignKey('apps.User', CASCADE, related_name='todos')
    title = CharField(max_length=255)
    completed = BooleanField(default=False)


class User(Model):
    name = CharField(max_length=255)
    username = CharField(max_length=255)
    email = EmailField(max_length=255)
    address  = CharField(max_length=255)
    phone = CharField(max_length=50)
    website = CharField(max_length=255)
    company = CharField(max_length=255)

