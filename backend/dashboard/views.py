id="vvnfr9"
from django.shortcuts import render

from accounts.models import Student
from complaints.models import Complaint
from leave_management.models import Leave
from payments.models import Payment
from food_menu.models import FoodMenu


def dashboard_ui(request):

    context = {

        'total_students': Student.objects.count(),

        'total_complaints': Complaint.objects.count(),

        'total_leaves': Leave.objects.count(),

        'total_payments': Payment.objects.count(),

    }

    return render(request, 'dashboard.html', context)


def students_ui(request):

    students = Student.objects.all()

    return render(request, 'students.html', {
        'students': students
    })


def leaves_ui(request):

    leaves = Leave.objects.all()

    return render(request, 'leaves.html', {
        'leaves': leaves
    })


def complaints_ui(request):

    complaints = Complaint.objects.all()

    return render(request, 'complaints.html', {
        'complaints': complaints
    })


def payments_ui(request):

    payments = Payment.objects.all()

    return render(request, 'payments.html', {
        'payments': payments
    })


def foodmenu_ui(request):

    foods = FoodMenu.objects.all()

    return render(request, 'foodmenu.html', {
        'foods': foods
    })
