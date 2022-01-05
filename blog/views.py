from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from blog.models import Post, BlogContact

from django.contrib import messages
from meta.views import Meta

# Create your views here.
from pages.models import HomePage, ContactPage


def posts(request):
    context = dict()

    page = HomePage.get_solo()

    meta = Meta(
        use_title_tag=True,
        use_facebook=True,
        use_twitter=True,
        title=page.seo_title,
        description=page.seo_description,
    )

    context['yourposts'] = Post.objects.all()
    context['page'] = page
    context['meta'] = meta


    return render(request, 'blog/posts.html', context)


def posts_search(request):
    context = dict()

    keywords = request.GET.get('keywords', '')

    context['posts'] = Post.objects.filter(
        title__icontains=keywords)  # icontains = insensitive (to uppercase/downcase) contains
    context['keywords'] = keywords

    return render(request, 'blog/posts_search.html', context)





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

    def get_context_data(self, **kwargs):
        ctx = super(BlogContactView, self).get_context_data(**kwargs)

        page = ContactPage.get_solo()

        meta = Meta(
            use_title_tag=True,
            use_facebook=True,
            use_twitter=True,
            title=page.seo_title,
            description=page.seo_description,
        )

        ctx['page'] = page
        ctx['meta'] = meta

        return ctx



#

class PostCreateView(CreateView):
    template_name = 'blog/post_add.html'
    # form_class = BlogContactForm
    model = Post
    fields = ['title', 'body', 'image', 'category']

    def get_success_url(self):
        return reverse('post_detail', kwargs={'id': self.object.id})

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Your post was created successfully.')
        response = super().form_valid(form)
        return response


# # function based views
# @login_required
# def post_detail(request, id):
#     context = dict()
#
#     # post = Post.objects.get(id=id)
#     post = get_object_or_404(Post, id=id)
#     context['post'] = post
#
#     return render(request, 'blog/post_detail.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

