from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.


def posts(request):

    context = dict()

    context['yourposts'] = Post.objects.all()

    return render(request, 'blog/posts.html', context)



def post_detail(request, id):

    context = dict()

    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    context['post'] = post

    return render(request, 'blog/post_detail.html', context)
