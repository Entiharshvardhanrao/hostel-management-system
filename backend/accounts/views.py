from django.shortcuts import render, redirect
from .models import Student
from complaints.models import Complaint

def student_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        student = Student.objects.filter(
            email=email,
            password=password
        ).first()

        if student:
            request.session["student_id"] = student.id
            return redirect("/student-dashboard/")

    return render(request, "student_login.html")


def student_dashboard(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/student-login/")

    student = Student.objects.get(id=student_id)

    return render(
        request,
        "student_dashboard.html",
        {
            "student": student
        }
    )
def student_complaint(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/student-login/")

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        Complaint.objects.create(
            student=student,
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )

        return redirect("/student-complaints/")

    return render(
        request,
        "student_complaint.html"
    )
def student_complaints(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/student-login/")

    complaints = Complaint.objects.filter(
        student_id=student_id
    ).order_by("-created_at")

    return render(
        request,
        "student_complaints.html",
        {
            "complaints": complaints
        }
    )
from leave_management.models import Leave


def apply_leave(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        Leave.objects.create(
            student=student,
            reason=request.POST.get("reason"),
            from_date=request.POST.get("from_date"),
            to_date=request.POST.get("to_date")
        )

        return redirect("/api/my-leaves/")

    return render(request, "apply_leave.html")


def my_leaves(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

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