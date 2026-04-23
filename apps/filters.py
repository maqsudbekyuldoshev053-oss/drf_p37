from django.db.models.aggregates import Count
from django_filters import FilterSet, NumberFilter

from apps.models import Post, Album, Photo, User, Comments


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ('userId',)



class AlbumFilter(FilterSet):

    class Meta:
        model = Album
        fields = ('userId',)


class PhotoFilter(FilterSet):

    class Meta:
        model = Photo
        fields = ('albumId',)


class UserFilter(FilterSet):

    class Meta:
        model = User
        fields = ('id',)


class CommentFilter(FilterSet):
    class Meta:
        model = Comments
        fields = ('postId',)
