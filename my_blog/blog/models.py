from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_on = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    # sort database results by created_on date, descending by default
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
