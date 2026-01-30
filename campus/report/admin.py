from django.contrib import admin
from .models import ActivityPoints

@admin.register(ActivityPoints)
class ActivityPointsAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'total_points')
    list_filter = ('semester',)
