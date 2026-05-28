from rest_framework import generics
from .models import Leave
from .serializers import LeaveSerializer


class LeaveListCreateView(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer