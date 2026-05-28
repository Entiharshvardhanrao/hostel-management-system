from django.db import models
from accounts.models import Student


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Paid', 'Paid'),
            ('Pending', 'Pending'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.student.name} - {self.amount}"