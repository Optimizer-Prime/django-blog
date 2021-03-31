from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


class Post(models.Model):
    """Defines the model for each blog post. """

    STATUS = (
        ('draft', "Draft"),
        ('published', "Published")
    )

    CATEGORY_CHOICES = [
        ('web-dev', 'Web Development'),
        ('data-sci', 'Data Science'),
        ('automation', 'Automation'),
        ('hardware', 'Hardware'),
        ('health', 'Health'),
        ('misc', 'Miscellaneous'),
        ('', 'None'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='')
    summary = models.CharField(max_length=255, default='')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)  # DateTime needed for better filtering
    last_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    is_featured = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    # sort database results by created_on date, descending because of '-'
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])


class PostImage(models.Model):
    """Allows additional images beyond the one defined in the Post class to be added and associated with a post."""
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


class Publication(models.Model):
    """Defines typical attributes of a scientific publication."""
    TYPE = [
        ('manuscript', 'Manuscript'),
        ('abstract', 'Abstract'),
    ]

    title = models.TextField()
    authors = models.TextField()
    year_published = models.IntegerField()
    article_type = models.CharField(max_length=255, choices=TYPE, default='abstract')
    journal_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=50, blank=True, null=True)
    issue = models.CharField(max_length=50, blank=True, null=True)
    doi = models.URLField(blank=True, null=True)

    journal_link = models.URLField(blank=True, null=True)
    download_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
