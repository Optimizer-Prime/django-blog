from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Post, Publication


def blog_list_view(request):
    """
    Returns main list and featured list of posts for homepage.
    :param request: standard parameter
    :return: request, html template to use, dict of different contexts
    """
    main_list = Post.objects.filter(status='published').order_by('-created_on')

    # returns the 3 most recent posts where is_featured = True
    featured_list = Post.objects.filter(status='published').filter(is_featured=True).order_by('-created_on')[:3]

    paginator = Paginator(main_list, 5)  # 5 items per page
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
    """Detailed view for each blog post."""
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

    paginator = Paginator(category_list, 5)  # 5 items per page
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


class AboutPageView(TemplateView):
    """Displays the about.html page as-is."""
    template_name = 'about.html'


def publications_view(request):
    """
    Returns publications_list for display on publications page.
    :param request: standard parameter
    :return: request, html template to use, dict of contexts
    """
    publications_list = Publication.objects.order_by('-year_published')

    context = {
        'publications_list': publications_list,
    }
    return render(request, 'publications.html', context)


class ContactView(TemplateView):
    """Displays contact page as-is."""
    template_name = 'contact.html'


class SearchResultsView(ListView):
    """Creates search result queryset using given query."""
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_results = Post.objects.filter(status='published').filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(summary__icontains=query)
        )
        return search_results

    # adding this makes search page display results
    context_object_name = 'search_results'
