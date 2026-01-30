import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from activities.models import Activity
from participation.models import Participation

User = get_user_model()

def run_verification():
    print("--- Starting Verification ---")
    c = Client()
    
    # 1. Setup Users
    admin = User.objects.get(username='admin')
    faculty, created = User.objects.get_or_create(username='faculty1', email='f1@test.com', role='FACULTY')
    if created: faculty.set_password('pass123'); faculty.save()
    student, created = User.objects.get_or_create(username='student1', email='s1@test.com', role='STUDENT')
    if created: student.set_password('pass123'); student.save()
    print("Users setup: OK")

    # 2. Faculty Creates Activity
    c.force_login(faculty)
    activity_data = {
        'title': 'Hackathon 2024',
        'category': 'TECHNICAL',
        'description': 'Coding event',
        'start_date': '2024-12-01T10:00',
        'end_date': '2024-12-02T10:00',
        'location': 'Lab 1',
        'max_participants': 50,
        'points': 20
    }
    response = c.post('/activities/create/', activity_data, follow=True)
    if response.status_code == 200:
        print("Faculty Create Activity: OK")
        activity = Activity.objects.get(title='Hackathon 2024')
    else:
        print(f"Faculty Create Activity: FAIL ({response.status_code})")
        return

    # 3. Student Applies
    c.force_login(student)
    response = c.post(f'/participation/apply/{activity.id}/', follow=True)
    if Participation.objects.filter(student=student, activity=activity, status='APPLIED').exists():
        print("Student Apply: OK")
    else:
        print("Student Apply: FAIL")
        return
        
    # 4. Faculty Verifies
    c.force_login(faculty)
    participation = Participation.objects.get(student=student, activity=activity)
    response = c.get(f'/participation/approve/{participation.id}/', follow=True)
    participation.refresh_from_db()
    if participation.status == 'APPROVED':
        print("Faculty Approve: OK")
    else:
        print(f"Faculty Approve: FAIL (Status: {participation.status})")

    # 5. Certificate Download
    c.force_login(student)
    response = c.get(f'/certificates/download/{participation.id}/')
    if response.status_code == 200 and 'attachment' in response['Content-Disposition']:
        print("Certificate Download: OK")
    else:
         print(f"Certificate Download: FAIL ({response.status_code})")

    print("--- Verification Complete ---")

if __name__ == '__main__':
    run_verification()
