id="s4c0ol"
from django.urls import path

from .views import (
    dashboard_ui,
    students_ui,
    leaves_ui,
    complaints_ui,
    payments_ui,
    foodmenu_ui
)

urlpatterns = [

    path('dashboard-ui/', dashboard_ui),

    path('students-ui/', students_ui),

    path('leaves-ui/', leaves_ui),

    path('complaints-ui/', complaints_ui),

    path('payments-ui/', payments_ui),

    path('foodmenu-ui/', foodmenu_ui),

]
