from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('home.html')
def show_featured_posts(count=3):
    """Returns 3 most recent posts where is_featured = True."""
    featured_posts = Post.objects.filter(status='published').filter(is_featured=True).order_by('-created_on')[:count]

    return {'featured_posts': featured_posts}
