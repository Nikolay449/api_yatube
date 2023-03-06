from rest_framework import serializers
from posts.models import Group, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
        model = Comment
