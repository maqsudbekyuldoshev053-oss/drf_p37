from django.db import models
from django.db.models import Model, TextField, CharField, EmailField, ForeignKey, CASCADE, URLField, \
    BooleanField, IntegerField, DecimalField
from django.db.models.fields import PositiveIntegerField, DateTimeField


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


class Book(Model):
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    published_year = IntegerField()
    is_available = BooleanField(default=True)





class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)

    def __str__(self):
        return self.name



class Order(Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    customer = ForeignKey('apps.Customer', CASCADE, related_name='orders')
    created_at = DateTimeField(auto_now_add=True)
    status = CharField(max_length=255, choices=STATUS_CHOICES, default='pending')


class OrderItem(Model):
    order = ForeignKey('apps.Order', CASCADE, related_name='items')
    product = ForeignKey('apps.Product', CASCADE, related_name='order_items')
    quantity = IntegerField()



class Student(Model):

    name = CharField(max_length=255)
    age = IntegerField()
    grade = CharField(max_length=1)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)


