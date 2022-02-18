from rest_framework import serializers
from .models import Memory


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['id','name', 'title', 'body', 'photo_url', 'social_url', ]
