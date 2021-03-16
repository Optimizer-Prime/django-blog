from django.contrib import admin
from .models import Post, PostImage, Publication


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ('title', 'slug', 'status', 'created_on', 'last_updated',)
    list_filter = ('status',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Publication)
