from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at']
    list_filter = ['created_at', 'category', 'author']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_post_count', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    def get_post_count(self, obj):
        return Post.objects.filter(category=obj).count()
    get_post_count.short_description = 'Post Count'

    