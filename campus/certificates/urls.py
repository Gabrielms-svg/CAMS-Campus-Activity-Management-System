from django.urls import path
from . import views

urlpatterns = [
    path('download/<int:participation_id>/', views.download_certificate, name='download_certificate'),
]
