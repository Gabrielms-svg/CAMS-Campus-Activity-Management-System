from django.db import models
from django.conf import settings
from activities.models import Activity

class Participation(models.Model):
    STATUS_CHOICES = (
        ('APPLIED', 'Applied'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    )

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='participations', limit_choices_to={'role': 'STUDENT'})
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='participations')
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_participations', limit_choices_to={'role': 'FACULTY'})

    class Meta:
        unique_together = ('student', 'activity')

    def __str__(self):
        return f"{self.student.username} - {self.activity.title}"
