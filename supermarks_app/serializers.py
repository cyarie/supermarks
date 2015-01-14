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
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmark-detail', read_only=True)

    class Meta:
        model = MarkUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'bookmarks')

    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.user.username = attrs.get('user.username', instance.user.username)
            instance.user.email = attrs.get('user.email', instance.user.email)
            instance.user.password = attrs.get('user.password', instance.user.password)
            instance.user.first_name = attrs.get('user.first_name', instance.user.first_name)
            instance.user.last_name = attrs.get('user.last_name', instance.user.last_name)
            return instance

        user = User.objects.create_user(username=attrs.get('user.username'),
                                        email=attrs.get('user.email'),
                                        password=attrs.get('user.password'))
        return MarkUser(user=user)
