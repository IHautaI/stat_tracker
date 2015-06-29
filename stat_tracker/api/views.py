from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from api.serializers import ActivitySerializer, EditActivitySerializer
from stats.models import Activity, Entry
from users.models import Profile


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            profile = Profile.objects.get(user=self.request.user)
            return profile.activity_set.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EditActivitySerializer(instance)
        return Response(serializer.data)
