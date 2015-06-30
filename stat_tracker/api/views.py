from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


from api.serializers import ActivitySerializer, EditActivitySerializer
from stats.models import Activity, Entry
from users.models import Profile


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return profile.activity_set.all()


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EditActivitySerializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

@api_view(['PUT', 'POST'])
def stats(request, pk):
    activity = Activity.objects.get(pk=pk)
    if activity.profile == request.user.profile:

        if request.method == 'POST':

            timestamp = request.POST.get('date')
            activity.entry_set.create(timestamp=timestamp)

            content = { 'date': timestamp,
                        'count': activity.entry_set.filter(\
                                  timestamp=timestamp).count()
            }

            return Response(content, status=status.HTTP_201_CREATED)

        elif request.method == 'PUT':
            timestamp = request.PUT.get('date')
            number = request.PUT.get('count')
            activity.entry_set.filter(timestamp=timestamp).delete()

            for _ in range(number):
                activity.entry_set.create(timestamp=timestamp)

            return Response(activity.entry_set.filter(timestamp=timestamp), status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@login_required
def rm_stats(request, pk):
    activity = Activity.objects.get(pk=pk)
    if activity.profile == request.user.profile:
        timestamp = request.DELETE.get('date')
        activity.entry_set.filter(timestamp=timestamp).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    else:

        return Response(status=status.HTTP_401_UNAUTHORIZED)
