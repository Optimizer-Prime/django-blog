from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post


# try and rewrite as fxn based view, incorporating featured as context option
class BlogListView(ListView):
    queryset = Post.objects.filter(status='published').order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'main_list'


class FeaturedView(ListView):
    queryset = Post.objects.filter(status='published').filter(is_featured=True).order_by('-created_on')
    # template_name = 'home.html'
    context_object_name = 'featured_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def category_list_view(request, category):
    category_list = Post.objects.filter(status='published').filter(category=category).order_by('-created_on')

    paginator = Paginator(category_list, 5)
    page_number = request.GET.get('page')

    try:
        category_list = paginator.page(page_number)
    except PageNotAnInteger:
        category_list = paginator.page(1)
    except EmptyPage:
        category_list = paginator.page(paginator.num_pages)

    context = {
        'category_list': category_list,
    }
    return render(request, 'category_home.html', context)


# just displays the defined template as the page
class AboutPageView(TemplateView):
    template_name = 'about.html'


class PublicationsView(TemplateView):
    template_name = 'publications.html'
