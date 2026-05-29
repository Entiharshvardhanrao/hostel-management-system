
from django.urls import path

from .views import (
    student_login,
    student_dashboard,
    student_complaint,
    student_complaints,
    apply_leave,
    my_leaves,
    student_food_menu,
    student_logout,
    student_payments
)

urlpatterns = [

    path(
        "student-login/",
        student_login
    ),

    path(
        "student-dashboard/",
        student_dashboard
    ),

    path(
        "raise-complaint/",
        student_complaint
    ),

    path(
        "student-complaints/",
        student_complaints
    ),

    path(
        "apply-leave/",
        apply_leave
    ),

    path(
        "my-leaves/",
        my_leaves
    ),

    path(
        "student-food-menu/",
        student_food_menu
    ),

    path(
        "student-logout/",
        student_logout
    ),

    path(
        "student-payments/",
        student_payments
    ),

]
