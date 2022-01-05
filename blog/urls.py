from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name="posts"),
    path('posts/search/', views.posts_search, name="posts_search"),
    path('posts/add/', views.PostCreateView.as_view(), name="post_add"),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),

    path('contact/', views.BlogContactView.as_view(), name="blog_contact"),
]
