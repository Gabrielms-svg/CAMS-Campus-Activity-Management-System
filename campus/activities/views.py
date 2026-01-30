from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Activity
from .forms import ActivityForm

def is_faculty(user):
    return user.role == 'FACULTY'

@login_required
@user_passes_test(is_faculty)
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.faculty_incharge = request.user
            activity.save()
            messages.success(request, 'Activity created successfully!')
            return redirect('faculty_dashboard')
    else:
        form = ActivityForm()
    return render(request, 'activities/activity_form.html', {'form': form, 'title': 'Create Activity'})

@login_required
@user_passes_test(is_faculty)
def update_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk, faculty_incharge=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity updated successfully!')
            return redirect('faculty_dashboard')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activities/activity_form.html', {'form': form, 'title': 'Update Activity'})

@login_required
@user_passes_test(is_faculty)
def faculty_activities(request):
    activities = Activity.objects.filter(faculty_incharge=request.user)
    return render(request, 'activities/faculty_activities.html', {'activities': activities})

def activity_list(request):
    activities = Activity.objects.filter(status='OPEN')
    return render(request, 'activities/activity_list.html', {'activities': activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activities/activity_detail.html', {'activity': activity})
