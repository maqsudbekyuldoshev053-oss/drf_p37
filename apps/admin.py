from django.contrib import admin
from apps.models import Post, Comments


@admin.register(Post)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'userId', 'title', 'body'


@admin.register(Comments)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = 'postId', 'name', 'email', 'body'




