from rest_framework import serializers

from stats.models import Activity, Entry
from users.models import Profile


class EntrySerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = Entry
        fields = ('date', 'count')

    def create(self, validated_data):
        entry = Entry.objects.create(**validated_data)
        return entry
        

class ActivitySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,view_name='activities-detail')
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Activity
        fields = ('url', 'id', 'title', 'description',)


    def create(self, validated_data):
        activity = Activity.objects.create(**validated_data)
        return activity


class EditActivitySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    stats = EntrySerializer(many=True)

    class Meta:
        model = Activity
        fields = ('title', 'description', 'stats')



    # def get_stats(self, obj):
    #     dates = obj.entry_set.values('timestamp').distinct()
    #     content = []
    #     for date in dates:
    #         content.append({'date': date, 'count': \
    #                         obj.entry_set.filter(timestamp=date).count()
    #                         })
    #
    #     return content
