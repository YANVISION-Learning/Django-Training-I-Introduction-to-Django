from django.contrib import admin
from blog.models import Post, PostCategory,BlogContact

# Register your models here.

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(BlogContact)
