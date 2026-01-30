from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:activity_id>/', views.apply_activity, name='apply_activity'),
    path('cancel/<int:participation_id>/', views.cancel_participation, name='cancel_participation'),
    path('manage/', views.manage_participation, name='manage_participation'),
    path('approve/<int:participation_id>/', views.approve_participation, name='approve_participation'),
    path('reject/<int:participation_id>/', views.reject_participation, name='reject_participation'),
]
