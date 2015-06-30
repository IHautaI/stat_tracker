from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


from api.serializers import ActivitySerializer, EditActivitySerializer, EntrySerializer
from stats.models import Activity, Entry
from users.models import Profile


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ["GET", "POST", "PUT", "DELETE"]


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
@login_required
def stats(request, pk):
    activity = Activity.objects.get(pk=pk)
    if activity.profile == request.user.profile:

        if request.method == 'POST':
            serializer = EntrySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(activity=activity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':

            serializer = EntrySerializer(request.data)

            if serializer.is_valid():
                date = serializer.data['date']
                queryset = activity.stats.filter(date=date)

                if queryset.exists():
                    activity = queryset[0]
                    activity.count = serializer.data['count']
                    activity.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

                return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@login_required
def rm_stats(request, pk):
    activity = Activity.objects.get(pk=pk)
    if activity.profile == request.user.profile:
        date = request.data.get('date')
        activity.entry_set.filter(date=date).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    else:

        return Response(status=status.HTTP_401_UNAUTHORIZED)
