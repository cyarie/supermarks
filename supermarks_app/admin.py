from django.contrib import admin
from supermarks_app.models import BookMark, Tag, MarkUser

admin.site.register(BookMark)
admin.site.register(Tag)
admin.site.register(MarkUser)
