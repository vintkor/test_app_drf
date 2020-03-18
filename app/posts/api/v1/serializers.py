from rest_framework import serializers
from posts.models import (
    Post,
    Like,
)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = (
            'user',
            'created',
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
