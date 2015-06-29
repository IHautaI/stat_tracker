from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'activity', views.ActivityViewSet, base_name='activity')

urlpatterns = [
    url(r'activities/(?P<pk>[0-9]+)/stats/$', views.stats),
    url(r'stats/(?P<pk>[0-9]+)$', views.rm_stats),
]

urlpatterns.extend(router.urls)
