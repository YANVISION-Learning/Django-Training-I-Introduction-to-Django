from django.db import models
from django_quill.fields import QuillField

from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = QuillField()
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('blog.PostCategory', on_delete=models.SET_NULL, null=True) # Or models.ForeignKey(PostCategory)

    image = ProcessedImageField(upload_to='posts/',
                                           format='JPEG',
                                           options={'quality': 80}, null=True)

    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(694, 300)],
                                      format='JPEG',
                                      options={'quality': 80})



    def __str__(self):
        return self.title


class PostCategory(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class BlogContact(models.Model):
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name
