from django.contrib import admin
from BL0G.models import Author, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
