import os
import django
from django.template.loader import render_to_string
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus.settings')
django.setup()

from activities.models import Activity

try:
    activity = Activity.objects.get(pk=2)
    context = {'activity': activity, 'user': activity.faculty_incharge} # approximate context
    try:
        rendered = render_to_string('activities/activity_detail.html', context)
        print("--- RENDERED OUTPUT START ---")
        if "Faculty In-charge: Bruce Mathews" in rendered or "Faculty In-charge: Bruce" in rendered:
            print("SUCCESS: Found rendered faculty name.")
        elif "{{ activity.faculty_incharge" in rendered:
            print("FAIL: Found literal template tag.")
        else:
            print("UNKNOWN: Checking grep...")
        
        # Print the specific lines
        for line in rendered.split('\n'):
            if "Faculty In-charge" in line:
                print(f"Line: {line.strip()}")
            if "Location:" in line:
                print(f"Line: {line.strip()}")
        print("--- RENDERED OUTPUT END ---")
        
    except Exception as e:
        print(f"Template Rendering Error: {e}")

except Exception as e:
    print(f"Setup Error: {e}")
