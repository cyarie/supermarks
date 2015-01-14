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
    password = serializers.CharField(source='user.password')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmark-detail', read_only=True)

    class Meta:
        model = MarkUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'bookmarks')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        markuser = MarkUser.user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        markuser.set_password(validated_data['user']['password'])
        markuser.save()
        return markuser
