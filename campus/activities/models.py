from django.db import models
from django.conf import settings

class Activity(models.Model):
    CATEGORY_CHOICES = (
        ('SPORTS', 'Sports'),
        ('ARTS', 'Arts'),
        ('TECHNICAL', 'Technical'),
        ('OTHER', 'Other'),
    )
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('CANCELLED', 'Cancelled'),
    )

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    description = models.TextField()
    faculty_incharge = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_activities', limit_choices_to={'role': 'FACULTY'})
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200, default='Campus')
    max_participants = models.PositiveIntegerField()
    points = models.PositiveIntegerField(default=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    image = models.ImageField(upload_to='activity_images/', blank=True, null=True)

    def __str__(self):
        return self.title
