from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, Category, Tag, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        modeel = User
        fields = ['id', 'username', 'email']

    
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    categories = serializers.ListField(child=serializers.CharField(), write_only=True)
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'categories', 'tags']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        
        # Remove categories and tags from validated_data
        categories_data = validated_data.pop('categories', [])
        tags_data = validated_data.pop('tags', [])
        
        # Remove the author field from validated_data if it exists
        validated_data.pop('author', None)

        # Create the post with the rest of the validated data
        post = Post.objects.create(author=user, **validated_data)
        
        # Handle categories
        categories = []
        for category_name in categories_data:
            category, created = Category.objects.get_or_create(name=category_name)
            categories.append(category)
        post.categories.set(categories)

        # Handle tags
        tags = []
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        post.tags.set(tags)

        return post
