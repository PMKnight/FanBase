from rest_framework import serializers
from .models import Memory


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['name', 'title', 'body', 'photo_url', 'social_url', ]
