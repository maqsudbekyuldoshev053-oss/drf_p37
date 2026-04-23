from django.urls import path
from apps.views import PostListCreateAPIView, \
    PostRetrieveUpdateDestroyAPIView, PostCommentsListAPIView, CommentsRetrieveUpdateDestroyAPIView, \
    AlbumListCreateAPIView, AlbumRetrieveUpdateDestroyAPIView, PhotoListCreateAPIView, TodoListCreateAPIView, \
    PhotoRetrieveUpdateDestroyAPIView, TodoRetrieveUpdateDestroyAPIView, AlbumPhotoListAPIView, UserListCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView, UserPostListAPIView, UserTodoListAPIView, UserAlbumListAPIView, \
    CommentsListCreateAPIView, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, ProductListCreateAPIView, \
    OrderListCreateAPIView, CustomerListCreateAPIView, OrderItemListCreateAPIView, StudentListCreateAPIView

urlpatterns = [
    path('posts', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<int:pk>/comments', PostCommentsListAPIView.as_view()),
    path('comments', CommentsListCreateAPIView.as_view()),
    path('comments/<int:pk>', CommentsRetrieveUpdateDestroyAPIView.as_view()),
    path('albums', AlbumListCreateAPIView.as_view()),
    path('albums/<int:pk>', AlbumRetrieveUpdateDestroyAPIView.as_view()),
    path('albums/<int:pk>/photo', AlbumPhotoListAPIView.as_view()),
    path('photos', PhotoListCreateAPIView.as_view()),
    path('photos/<int:pk>', PhotoRetrieveUpdateDestroyAPIView.as_view()),
    path('todos', TodoListCreateAPIView.as_view()),
    path('todos/<int:pk>', TodoRetrieveUpdateDestroyAPIView.as_view()),
    path('users', UserListCreateAPIView.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/<int:pk>/posts', UserPostListAPIView.as_view()),
    path('users/<int:pk>/todos', UserTodoListAPIView.as_view()),
    path('users/<int:pk>/albums', UserAlbumListAPIView.as_view()),
    path('books', BookListCreateAPIView.as_view()),
    path('books/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('products', ProductListCreateAPIView.as_view()),
    path('customer', CustomerListCreateAPIView.as_view()),
    path('order', OrderListCreateAPIView.as_view()),
    path('ordersItems', OrderItemListCreateAPIView.as_view()),
    path('students', StudentListCreateAPIView.as_view())
]

