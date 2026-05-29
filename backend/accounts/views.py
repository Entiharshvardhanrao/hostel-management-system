from django.shortcuts import render, redirect
from .models import Student
from complaints.models import Complaint
from leave_management.models import Leave
from food_menu.models import FoodMenu
from payments.models import Payment

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

            return redirect("/api/student-dashboard/")

    return render(
        request,
        "student_login.html"
    )


def student_dashboard(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

    student = Student.objects.get(id=student_id)

    complaint_count = Complaint.objects.filter(
        student=student
    ).count()

    leave_count = Leave.objects.filter(
        student=student
    ).count()

    return render(
        request,
        "student_dashboard.html",
        {
            "student": student,
            "complaint_count": complaint_count,
            "leave_count": leave_count,
        }
    )


def student_complaint(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        Complaint.objects.create(
            student=student,
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )

        return redirect("/api/student-complaints/")

    return render(
        request,
        "student_complaint.html"
    )


def student_complaints(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

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

    return render(
        request,
        "apply_leave.html"
    )


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


def student_food_menu(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

    menus = FoodMenu.objects.all()

    return render(
        request,
        "student_food_menu.html",
        {
            "menus": menus
        }
    )


def student_logout(request):

    request.session.flush()

    return redirect("/api/student-login/")

def student_payments(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("/api/student-login/")

    payments = Payment.objects.filter(
        student_id=student_id
    ).order_by("-payment_date")

    total_amount = sum(
        payment.amount
        for payment in payments
    )

    paid_amount = sum(
        payment.amount
        for payment in payments
        if payment.status == "Paid"
    )

    pending_amount = total_amount - paid_amount

    return render(
        request,
        "student_payments.html",
        {
            "payments": payments,
            "total_amount": total_amount,
            "paid_amount": paid_amount,
            "pending_amount": pending_amount,
        }
    )