from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

featured_post = Post.objects.get(slug='test-post')


class BlogListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# just displays the defined template as the page
class AboutPageView(TemplateView):
    template_name = 'about.html'
