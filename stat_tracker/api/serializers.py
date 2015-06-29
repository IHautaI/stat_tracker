from rest_framework import serializers

from stats.models import Activity, Entry
from users.models import Profile


class EntrySerializer(serializers.Serializer):
    timestamp = serializers.DateField()


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Activity
        fields = ('url', 'title', 'description',)


class EditActivitySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    entries = serializers.HyperlinkedIdentityField(view_name='stats')
    entry_set = EntrySerializer(many=True)

    class Meta:
        model = Activity
        fields = ('title', 'description', 'entry_set',)
