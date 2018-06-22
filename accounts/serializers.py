from rest_framework import serializers
from accounts.models import Berry


class BerrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Berry
        fields = ('id', 'email', 'nickname', 'created_at')


class BerryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berry
        fields = ('id', 'email', 'nickname', 'created_at')
