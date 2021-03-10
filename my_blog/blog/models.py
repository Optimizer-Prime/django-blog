from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
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

    # sort database results by created_on date, descending by default
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title
