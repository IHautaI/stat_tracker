from rest_framework import serializers


from stats.models import Activity, Entry
from users.models import Profile


class ActivitySerlializer(serializers.HyperlinkedModelSerializer):
    
