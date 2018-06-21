from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    article_id = serializers.IntegerField(required=True, allow_null=False)
    contents = serializers.CharField(required=True, allow_blank=False, max_length=1000)

    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.contents = validated_data.get('contents', instance.contents)
        instance.save()
        return instance


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'article_id', 'depth', 'contents', 'created_at')
