from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    category_list_view,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),

    # passes what's in <category>, which is defined in 'category_home.html' url tag for each link,
    # as variable named category to category_list_view in views.py
    path('category/<category>/', category_list_view, name='category_home'),
]
