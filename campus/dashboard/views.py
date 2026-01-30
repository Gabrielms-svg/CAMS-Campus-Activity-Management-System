from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    user = request.user
    if user.role == 'ADMIN':
        return redirect('admin_dashboard')
    elif user.role == 'FACULTY':
        return redirect('faculty_dashboard')
    elif user.role == 'STUDENT':
        return redirect('student_dashboard')
    return redirect('home')

@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def faculty_dashboard(request):
    if request.user.role != 'FACULTY':
        return redirect('dashboard')
    return render(request, 'dashboard/faculty_dashboard.html')

@login_required
def student_dashboard(request):
    if request.user.role != 'STUDENT':
        return redirect('dashboard')
    
    # Get student's participations
    participations = request.user.participations.all().order_by('-applied_on')
    
    # Check if we should calculate points dynamically since Report app is complex
    total_points = sum(p.activity.points for p in participations if p.status in ['APPROVED', 'COMPLETED'])
    
    context = {
        'participations': participations,
        'total_points': total_points
    }
    return render(request, 'dashboard/student_dashboard.html', context)
