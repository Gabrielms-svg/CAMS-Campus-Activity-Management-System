from django.db import models
from django.conf import settings

# This can be used for caching or aggregating points if needed, 
# otherwise we can calculate on the fly.
class ActivityPoints(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grade_card')
    semester = models.CharField(max_length=20)
    total_points = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('student', 'semester')

    def __str__(self):
        return f"{self.student.username} - {self.semester}"
