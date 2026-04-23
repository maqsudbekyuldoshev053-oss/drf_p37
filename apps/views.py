from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import request
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from apps.filters import PostFilter, AlbumFilter, PhotoFilter, UserFilter, CommentFilter
from apps.models import Post, Comments, Album, Photo, Todo, User, Book, Product, Customer, Order, OrderItem, Student
from apps.serializers import PostModelSerializer, CommentModelSerializer, AlbumModelSerializer, PhotoModelSerializer, \
    TodoModelSerializer, UserModelSerializer, BookModelSerializer, BookDetailModelSerializer, ProductSerializer, \
    CustomerSerializer, OrderSerializer, OrderItemSerializer, StudentSerializer, StudentDetailSerializer


@extend_schema(tags=['Post'])
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter


@extend_schema(tags=['Post'])
class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer



@extend_schema(tags=['Post'])
class PostCommentsListAPIView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentModelSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        return qs.filter(postId=pk)


@extend_schema(tags=['Comment'])
class CommentsListCreateAPIView(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterest_fields = ('postId', 'email')
    search_fields = ('email', 'name')
    ordering_fields = ('postId', 'id')
    filterset_class = CommentFilter


@extend_schema(tags=['Comment'])
class CommentsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentModelSerializer


@extend_schema(tags=['Album'])
class AlbumListCreateAPIView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterest_fields = ('userId', 'id')
    search_fields = ('title',)
    filterset_class = AlbumFilter




@extend_schema(tags=['Album'])
class AlbumRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


@extend_schema(tags=['Album'])
class AlbumPhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        return qs.filter(albumId=pk)


@extend_schema(tags=['Photo'])
class PhotoListCreateAPIView(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterest_fields = ('albumId', 'id')
    search_fields = ('title',)
    filterset_class = PhotoFilter


@extend_schema(tags=['Photo'])
class PhotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer



@extend_schema(tags=['Todo'])
class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterest_fields = ('albumId', 'id')
    search_fields = ('title',)


@extend_schema(tags=['Todo'])
class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


@extend_schema(tags=['User'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterest_fields = ('albumId', 'id')
    search_fields = ('title',)
    filterset_class = UserFilter


@extend_schema(tags=['User'])
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['User'])
class UserPostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        return qs.filter(userId=pk)


@extend_schema(tags=['User'])
class UserTodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        return qs.filter(userId=pk)


@extend_schema(tags=['User'])
class UserAlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        return qs.filter(userId=pk)



@extend_schema(tags=['Book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title',)


@extend_schema(tags=['Book'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookDetailModelSerializer


@extend_schema(tags=['Product'])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



@extend_schema(tags=['Customer'])
class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



@extend_schema(tags=['Order'])
class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(tags=['OrderItem'])
class OrderItemListCreateAPIView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from .models import Student
from .serializers import StudentSerializer


@extend_schema(tags=['Student'])
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = (DjangoFilterBackend,SearchFilter, OrderingFilter)
    filterset_fields = ('grade', 'is_active')
    search_fields = ('name',)
    ordering_fields = ('age', 'created_at')









