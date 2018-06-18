from rest_framework import serializers
from boards.models import Board


class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    body = serializers.CharField(required=True, allow_blank=False, max_length=2000)
    views = serializers.IntegerField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = Board
        fields = ('id', 'title', 'views', 'created_at')
