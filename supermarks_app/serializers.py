from django.forms import widgets
from rest_framework import serializers
from supermarks_app.models import MarkUser, BookMark, Tag, User


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
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmark-detail', read_only=True)

    class Meta:
        model = MarkUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bookmarks')

    def create(self, validated_data):
        return MarkUser.objects.create(**validated_data)
