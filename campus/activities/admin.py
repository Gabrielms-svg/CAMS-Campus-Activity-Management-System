from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'start_date', 'faculty_incharge')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description')
