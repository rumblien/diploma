from django.shortcuts import render

from apps.accounts.models import User
def track_progress (request, student_id):

    total_lessons = 100
    completed_lessons = 75
    progress_percentage = (completed_lessons / total_lessons) * 100
    return render(request, 'student_progress.html', {'progress_percentage': progress_percentage})
