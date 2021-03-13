from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('web_dev', 'Web Development'),
        ('data_sci', 'Data Science'),
        ('automation', 'Automation'),
        ('hardware', 'Hardware'),
        ('medicine', 'Medicine'),
        ('misc', 'Miscellaneous'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='misc')
    summary = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)  # DateTime needed for better filtering
    last_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager(blank=True)

    # sort database results by created_on date, descending because of '-'
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title
