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

    categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Category.objects.all()
    )
    tags = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'categories', 'tags']
        
        def create(self, validated_data):
            # Automatically set the author to the current logged-in user
            request = self.context.get('request')
            user = request.user if request else None
            validated_data['author'] = user
            return super().create(validated_data)