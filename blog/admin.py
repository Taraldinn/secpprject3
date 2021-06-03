from django.contrib import admin

from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'sort_description',
        'description',
        'thumbnail',
        'creation'

    ]

    summernote_fields = ('description',)


admin.site.register(Post, PostAdmin)


class PostComment(admin.ModelAdmin):
    list_display = [
        'name',
        'body'
    ]


admin.site.register(Comment, PostComment)
