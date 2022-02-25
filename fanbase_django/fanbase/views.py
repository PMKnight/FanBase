from rest_framework import generics

# Create views here.
from .models import Memory

from .serializers import MemorySerializer


class MemoryList(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
