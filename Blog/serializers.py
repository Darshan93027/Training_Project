# posts/serializers.py
from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'author', 'created_at', 'updated_at', 'posts']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_posts(self, obj):
        posts = Post.objects.filter(category=obj)
        return PostSerializer(posts, many=True).data


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'category_name', 'created_at', 'updated_at']
        
