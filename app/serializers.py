from rest_framework import serializers
from .models import user, activity, duplicate
from rest_framework.settings import api_settings


class activityserializer(serializers.ModelSerializer):
    class Meta:
        model = activity
        fields = ['start_time', 'end_time']


class userserializer(serializers.ModelSerializer):
    activity_period = activityserializer(many=True, source='activity_periods')

    class Meta:
        model = user
        fields = ['id', 'real_name', 'tz','activity_period']


class duplicateserializer(serializers.ModelSerializer):
    members = userserializer(many=True, source='member')

    class Meta:
        model = duplicate
        fields = ['ok', 'members']
