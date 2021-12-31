from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name="posts"),
    path('posts/search/', views.posts_search, name="posts_search"),
    path('posts/<int:id>/', views.post_detail, name="post_detail"),


    path('contact/', views.BlogContactView.as_view(), name="blog_contact"),
]
