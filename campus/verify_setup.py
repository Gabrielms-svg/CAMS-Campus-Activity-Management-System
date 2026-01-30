import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def run_checks():
    c = Client()
    
    # Check Home Page
    response = c.get('/')
    print(f"Home Page Status: {response.status_code}")
    if response.status_code == 200:
        print("Home Page CHECK: PASS")
    else:
        print("Home Page CHECK: FAIL")

    # Check Login Page
    response = c.get('/accounts/login/')
    print(f"Login Page Status: {response.status_code}")
    if response.status_code == 200:
        print("Login Page CHECK: PASS")
    else:
        print("Login Page CHECK: FAIL")

    # Check Admin Login
    login_success = c.login(username='admin', password='adminpass')
    if login_success:
        print("Admin Login CHECK: PASS")
        # Check Dashboard Redirect
        response = c.get('/dashboard/')
        print(f"Dashboard Response Status: {response.status_code} (Redirect is 302)")
        if response.status_code == 302 and response.url == '/dashboard/admin/':
            print("Dashboard Admin Redirect CHECK: PASS")
        else:
             print(f"Dashboard Admin Redirect CHECK: FAIL (Got {response.status_code} to {getattr(response, 'url', '')})")
    else:
        print("Admin Login CHECK: FAIL")

if __name__ == '__main__':
    run_checks()
