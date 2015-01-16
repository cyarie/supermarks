from django.forms import widgets
from rest_framework import serializers
from supermarks_app.models import BookMark, Tag, MarkUser


class BookMarkSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = BookMark
        fields = ('bookmark_id', 'long_url', 'short_url', 'title', 'tags', 'category')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_id', 'tag')


class MarkUserSerializer(serializers.ModelSerializer):
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmark-detail', read_only=True)

    class Meta:
        model = MarkUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'bookmarks')
        extra_kwargs = {'password': {'write_only': True}}
