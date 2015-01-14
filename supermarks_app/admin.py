from django.contrib import admin
from supermarks_app.models import BookMarks, Tags, MarkUsers

admin.site.register(BookMarks)
admin.site.register(Tags)
admin.site.register(MarkUsers)
