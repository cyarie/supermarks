from django.contrib import admin
from supermarks_app.models import BookMark, Tag, User

admin.site.register(BookMark)
admin.site.register(Tag)
admin.site.register(User)
