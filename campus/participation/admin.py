from django.contrib import admin
from .models import Participation

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('student', 'activity', 'status', 'applied_on')
    list_filter = ('status',)
    search_fields = ('student__username', 'activity__title')
