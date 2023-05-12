from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.models import Staff,Staff_Notifications,Staff_leave


@login_required(login_url='/')
def HOME(request):
    return render(request, 'staff/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id


        notification = Staff_Notifications.objects.filter(staff_id = staff_id)

        context = {
            'notification':notification,
        }
    return render(request,'staff/notification.html',context)


@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notifications.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)

        context = {
            'staff_leave_history':staff_leave_history,
        }
    return render(request,'staff/apply_leave.html',context)


@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave(
            staff_id = staff,
            data = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request,'Leave Successfully Sent')
        return redirect('staff_apply_leave')