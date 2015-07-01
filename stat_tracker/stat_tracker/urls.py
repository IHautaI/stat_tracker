from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view()),
    url(r'api/', include('api.urls')),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', views.register),
    #url(r'users/', include('users.urls', namespace='users')),
    #url(r'accounts/', include('django.contrib.auth.urls', namespace='accounts')),
]
