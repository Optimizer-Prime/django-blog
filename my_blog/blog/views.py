from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from .models import Post


def blog_list_view(request):
    """
    Returns main list and featured list of posts for homepage.
    :param request: standard parameter
    :return: request, html template to use, dict of different contexts
    """
    main_list = Post.objects.filter(status='published').order_by('-created_on')

    # returns the 3 most recent posts where is_featured = True
    featured_list = Post.objects.filter(status='published').filter(is_featured=True).order_by('-created_on')[:3]

    paginator = Paginator(main_list, 5)
    page_number = request.GET.get('page')

    try:
        main_list = paginator.page(page_number)
    except PageNotAnInteger:
        main_list = paginator.page(1)
    except EmptyPage:
        main_list = paginator.page(paginator.num_pages)

    context = {
        'main_list': main_list,
        'featured_list': featured_list,
    }
    return render(request, 'home.html', context)


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def category_list_view(request, category):
    """
    Returns list view of posts filtered based on category.
    :param request: standard parameter
    :param category: passed as kwarg from <category> tag in url
    :return: request, html template to use, dict of different contexts
    """
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


class ContactView(TemplateView):
    template_name = 'contact.html'
