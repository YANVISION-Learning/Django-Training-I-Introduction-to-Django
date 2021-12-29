from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name="posts"),
    path('posts/<int:id>/', views.post_detail, name="post_detail"),
]
