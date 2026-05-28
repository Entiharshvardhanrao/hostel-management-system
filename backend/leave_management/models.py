from django.db import models
from accounts.models import Student


class Leave(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.student.name} - {self.status}"