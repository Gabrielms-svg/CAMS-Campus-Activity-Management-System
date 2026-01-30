from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('<int:pk>/', views.activity_detail, name='activity_detail'),
    path('create/', views.create_activity, name='create_activity'),
    path('update/<int:pk>/', views.update_activity, name='update_activity'),
    path('my-activities/', views.faculty_activities, name='faculty_activities'),
]
