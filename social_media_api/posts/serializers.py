from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post objects.
    """

    author = serializers.ReadOnlyField(source='author.username')
    comments_count = serializers.IntegerField(
        source='comments.count',
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'content',
            'comments_count',
            'created_at',
            'updated_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment objects.
    """

    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'content',
            'created_at',
            'updated_at',
        ]
