from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
