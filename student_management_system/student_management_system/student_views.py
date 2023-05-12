
from django.shortcuts import render, redirect
from app.models import Student_Notification,Student

@login_required(login_url='/')
def Home(request):
    return render(request,'Student/home.html')


@login_required(login_url='/')
def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification':notification,
        }
        return render(request,'Student/notification.html',context)



@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification =Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')