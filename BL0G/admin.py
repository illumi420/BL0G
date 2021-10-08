from django.contrib import admin
from .models import Author, Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date')
    list_filter = ("status", "categories")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

# Register your models here.


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
