from django.shortcuts import render, redirect
from app.models import Student_Notification, Student, Student_Feedback, Student_leave
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/')
def Home(request):
    return render(request, 'Student/home.html')


@login_required(login_url='/')
def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id=student_id)

        context = {
            'notification': notification,
        }
        return render(request, 'Student/notification.html', context)


@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')


@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id=student_id)
    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'student/feedback.html', context)


@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)

        feedbacks = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply="",
        )

        feedbacks.save()
        return redirect('student_feedback')
    return None


@login_required(login_url='/')
def STUDENT_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id=student)

    context = {
        'student_leave_history': student_leave_history,
    }

    return render(request, 'student/apply_leave', context)


@login_required(login_url='/')
def STUDENT_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_id = Student.objects.get(admin=request.user.id)

        leave = Student_leave(
            student_id=student_id,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Successfully Sent')
        return redirect('student_leave')
