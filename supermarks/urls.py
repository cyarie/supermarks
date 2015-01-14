from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from supermarks_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookmarks', views.BookMarkViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^', include(router.urls)),
)
