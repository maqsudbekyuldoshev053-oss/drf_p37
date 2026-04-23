from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.models import Post, Comments, Album, Photo, Todo, User, Book, Product, Order, Customer, OrderItem, Student


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class AlbumModelSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class PhotoModelSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class BookModelSerializer(ModelSerializer):
    is_expensive = SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'


    def validate_price(self, val):
        if val < 0:
            raise ValidationError('Price 0 dan kichik bo‘lmasligi kerak')
        return val

    def validate_published_year(self, val):
        if val < 1900:
            raise ValidationError('Published year 1900 dan kichik bo‘lmasligi kerak')
        return val

    def get_is_expensive(self, obj):
        return obj.price > 100

    def validate(self, data):
        if data['title'] == data['author']:
            raise ValidationError("title author bilan bir hil bulmasligi kerak")
        return data



class BookDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    is_adult = SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'

    def get_is_adult(self, obj):
        return obj.age > 18

    def validate_age(self, val):
        if val < 5:
            raise ValidationError("age 5 dan katta bulishi kerak")
        return val

    def validate_grade(self, val):
        if val != ['A', 'B', 'C']:
            raise ValidationError('Grade A, B, C  larga teng  bulishi kerak')
        return val

class StudentDetailSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



