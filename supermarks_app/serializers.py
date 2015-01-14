from django.forms import widgets
from rest_framework import serializers
from supermarks_app.models import User, BookMark, Tag


class BookMarkSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = BookMark
        fields = ('bookmark_id', 'long_url', 'short_url', 'title', 'tags', 'category')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_id', 'tag')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bookmarks = BookMarkSerializer(source='bookmark_group', many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bookmarks')
