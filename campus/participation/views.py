from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Participation
from activities.models import Activity

def is_student(user):
    return user.role == 'STUDENT'

def is_faculty(user):
    return user.role == 'FACULTY'

@login_required
@user_passes_test(is_student)
def apply_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == 'POST':
        # Check if already applied
        if Participation.objects.filter(student=request.user, activity=activity).exists():
            messages.warning(request, 'You have already applied for this activity.')
        else:
            if activity.status != 'OPEN':
                messages.error(request, 'This activity is not open for registration.')
            elif activity.participations.count() >= activity.max_participants:
                 messages.error(request, 'Registration full.')
            else:
                Participation.objects.create(student=request.user, activity=activity)
                messages.success(request, 'Successfully applied!')
    return redirect('activity_detail', pk=activity_id)

@login_required
@user_passes_test(is_student)
def cancel_participation(request, participation_id):
    participation = get_object_or_404(Participation, pk=participation_id, student=request.user)
    if participation.status == 'APPLIED':
        participation.status = 'CANCELLED'
        participation.save()
        messages.success(request, 'Participation cancelled.')
    else:
        messages.error(request, 'Cannot cancel at this stage.')
    return redirect('student_dashboard')

@login_required
@user_passes_test(is_faculty)
def manage_participation(request):
    # Get activities managed by this faculty
    activities = Activity.objects.filter(faculty_incharge=request.user)
    # Get pending participations for these activities
    participations = Participation.objects.filter(activity__in=activities, status='APPLIED')
    return render(request, 'participation/manage_participation.html', {'participations': participations})

@login_required
@user_passes_test(is_faculty)
def approve_participation(request, participation_id):
    participation = get_object_or_404(Participation, pk=participation_id, activity__faculty_incharge=request.user)
    participation.status = 'APPROVED'
    participation.verified_by = request.user
    participation.save()
    messages.success(request, f'Approved {participation.student.username}.')
    return redirect('manage_participation')

@login_required
@user_passes_test(is_faculty)
def reject_participation(request, participation_id):
    participation = get_object_or_404(Participation, pk=participation_id, activity__faculty_incharge=request.user)
    participation.status = 'REJECTED'
    participation.verified_by = request.user
    participation.save()
    messages.success(request, f'Rejected {participation.student.username}.')
    return redirect('manage_participation')
