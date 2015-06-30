from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'activities', views.ActivityViewSet, base_name='activities')

urlpatterns = [
    url(r'activities/(?P<pk>[0-9]+)/stats/$', views.stats),
    url(r'stats/(?P<pk>[0-9]+)$', views.rm_stats),
]

urlpatterns.extend(router.urls)
