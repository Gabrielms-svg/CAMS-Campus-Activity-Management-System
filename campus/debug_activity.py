import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus.settings')
django.setup()

from activities.models import Activity
from django.conf import settings

print(f"MEDIA_URL: '{settings.MEDIA_URL}'")
print(f"MEDIA_ROOT: '{settings.MEDIA_ROOT}'")

try:
    # User was accessing /activities/2/
    activity = Activity.objects.get(pk=2)
    print(f"Activity ID: {activity.pk}")
    print(f"Title: '{activity.title}'")
    print(f"Location: '{activity.location}'")
    
    if activity.image:
        print(f"Image Field: '{activity.image}'")
        print(f"Image URL: '{activity.image.url}'")
        full_path = activity.image.path
        print(f"Image Path: '{full_path}'")
        print(f"File Exists: {os.path.exists(full_path)}")
    else:
        print("Image: None")

    print(f"Faculty: {activity.faculty_incharge.username}")
    print(f"Faculty Full Name: '{activity.faculty_incharge.get_full_name()}'")

except Activity.DoesNotExist:
    print("Activity 2 not found.")
except Exception as e:
    print(f"Error: {e}")
