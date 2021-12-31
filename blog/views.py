from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from blog.models import Post, BlogContact

from django.contrib import messages


# Create your views here.


def posts(request):
    context = dict()

    context['yourposts'] = Post.objects.all()

    return render(request, 'blog/posts.html', context)


def posts_search(request):
    context = dict()

    keywords = request.GET.get('keywords', '')

    context['posts'] = Post.objects.filter(
        title__icontains=keywords)  # icontains = insensitive (to uppercase/downcase) contains
    context['keywords'] = keywords

    return render(request, 'blog/posts_search.html', context)


# function based views
def post_detail(request, id):
    context = dict()

    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    context['post'] = post

    return render(request, 'blog/post_detail.html', context)


# Class based views :
# Follow the pep8 norm in nomination
class BlogContactView(CreateView):
    template_name = 'blog/contact.html'
    # form_class = BlogContactForm
    model = BlogContact
    fields = ['name', 'subject', 'message']
    success_url = reverse_lazy('blog_contact', kwargs={})

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Your message was sent.')
        response = super().form_valid(form)
        return response


#

class PostDetailView(DetailView):
    pass
