from django.urls import path
from .views import LeaveListCreateView

urlpatterns = [
    path('leaves/', LeaveListCreateView.as_view()),
]
