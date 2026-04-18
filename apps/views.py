from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.models import Post, Comments, Album, Photo, Todo, User
from apps.serializers import PostModelSerializer, CommentModelSerializer, AlbumModelSerializer, PhotoModelSerializer, \
    TodoModelSerializer, UserModelSerializer


@extend_schema(tags=['Post'])
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


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


@extend_schema(tags=['Comment'])
class CommentsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentModelSerializer


@extend_schema(tags=['Album'])
class AlbumListCreateAPIView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


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


@extend_schema(tags=['Photo'])
class PhotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer


@extend_schema(tags=['Todo'])
class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


@extend_schema(tags=['Todo'])
class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


@extend_schema(tags=['User'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


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
