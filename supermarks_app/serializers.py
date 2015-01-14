from django.forms import widgets
from rest_framework import serializers
from supermarks_app.models import MarkUser, BookMark, Tag


class BookMarkSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = BookMark
        fields = ('bookmark_id', 'long_url', 'short_url', 'title', 'tags', 'category')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_id', 'tag')


class MarkUserSerializer(serializers.HyperlinkedModelSerializer):
    bookmarks = serializers.StringRelatedField(many=True)

    class Meta:
        model = MarkUser
        fields = 'bookmarks'
