from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, PostImage, Publication


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(SummernoteModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ('title', 'slug', 'status', 'created_on', 'last_updated',)
    list_filter = ('status',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Publication)
