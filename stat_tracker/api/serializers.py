from rest_framework import serializers

from stats.models import Activity, Entry
from users.models import Profile


# class EntrySerializer(serializers.Serializer):
#     timestamp = serializers.DateField()


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Activity
        fields = ('url', 'title', 'description',)


class EditActivitySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    stats = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ('title', 'description', 'stats')

    def get_stats(self, obj):
        dates = obj.entry_set.values('timestamp').distinct()
        content = []
        for date in dates:
            content.append({'date': date, 'count': \
                            obj.entry_set.filter(timestamp=date).count()
                            })

        return content
