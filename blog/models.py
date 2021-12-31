from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField() # Implement RichText Here
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/", null=True)
    category = models.ForeignKey('blog.PostCategory', on_delete=models.SET_NULL, null=True) # Or models.ForeignKey(PostCategory)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return "Category name: " + self.title


class BlogContact(models.Model):
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name
