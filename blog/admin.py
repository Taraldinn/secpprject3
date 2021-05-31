from django.contrib import admin

from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'sort_description',
        'description',
        'thumbnail',

    ]

    summernote_fields = ('description',)


admin.site.register(Post, PostAdmin)


class PostComment(admin.ModelAdmin):
    list_display = [
        'name',
        'body'
    ]


admin.site.register(Comment, PostComment)
