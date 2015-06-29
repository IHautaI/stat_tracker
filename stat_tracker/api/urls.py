from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'activity', views.ActivityViewSet, base_name='activity')

urlpatterns = []

urlpatterns.extend(router.urls)
