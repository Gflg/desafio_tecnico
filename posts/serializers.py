from posts.models import Posts
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title', 'content', 'author', 'theme', 'created_at')