from rest_framework import generics
from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintListCreateView(generics.ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer