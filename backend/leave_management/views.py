from rest_framework import generics
from .models import Leave
from .serializers import LeaveSerializer
from leave_management.models import Leave


class LeaveListCreateView(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

def apply_leave(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/student-login/")

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        Leave.objects.create(
            student=student,
            reason=request.POST.get("reason"),
            from_date=request.POST.get("from_date"),
            to_date=request.POST.get("to_date")
        )

        return redirect("/my-leaves/")

    return render(
        request,
        "apply_leave.html"
    )
def my_leaves(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/student-login/")

    leaves = Leave.objects.filter(
        student_id=student_id
    ).order_by("-id")

    return render(
        request,
        "my_leaves.html",
        {
            "leaves": leaves
        }
    )