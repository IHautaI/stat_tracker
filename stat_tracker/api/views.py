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

    # def get_serializer(self, *args, **kwargs):
    #     if self.request.method in ['GET', 'POST', 'DELETE']:
    #         return super().get_serializer(*args, **kwargs)
    #
    #     if self.request.method in ['PUT']:
    #         serializer_class = EditActivitySerializer
    #         kwargs['context'] = self.get_serializer_context()
    #         return serializer_class(*args, **kwargs)

    # def perform_update(self, serializer):
    #     stats = self.request.data['stats']
    #     activity = serializer.save()
    #
    #     serializer = EntrySerializer(stats)
    #     activity.entry_set.create()


@api_view(['PUT', 'POST'])
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
            date = request.PUT.get('date')
            count = request.PUT.get('count')
            queryset = activity.stats.filter(date=date)
            if queryset:
                activity = queryset[0]
                activity.count = count
                activity.save()
                return Response({"date":date, "count":count}, status=status.HTTP_200_OK)
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
        date = request.DELETE.get('date')
        activity.entry_set.filter(date=date).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    else:

        return Response(status=status.HTTP_401_UNAUTHORIZED)
