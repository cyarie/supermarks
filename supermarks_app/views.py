from supermarks_app.models import MarkUser, BookMark, Tag
from rest_framework import viewsets
from supermarks_app.serializers import MarkUserSerializer, BookMarkSerializer, TagSerializer


class MarkUserViewSet(viewsets.ModelViewSet):
    queryset = MarkUser.objects.all()
    serializer_class = MarkUserSerializer


class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer