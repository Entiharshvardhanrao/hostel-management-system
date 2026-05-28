from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Student
from complaints.models import Complaint
from leave_management.models import Leave
from payments.models import Payment


class DashboardAPIView(APIView):

    def get(self, request):

        data = {
            "total_students": Student.objects.count(),

            "total_complaints": Complaint.objects.count(),

            "pending_complaints": Complaint.objects.filter(
                status='Pending'
            ).count(),

            "total_leaves": Leave.objects.count(),

            "approved_leaves": Leave.objects.filter(
                status='Approved'
            ).count(),

            "total_payments": Payment.objects.count(),

            "paid_payments": Payment.objects.filter(
                status='Paid'
            ).count(),
        }

        return Response(data)