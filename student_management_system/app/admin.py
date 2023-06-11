from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Staff_Notifications)
admin.site.register(Staff_leave)
admin.site.register(Staff_Feedback)
admin.site.register(Student_Notification)
admin.site.register(Student_Feedback)
admin.site.register(Student_leave)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(StudentResult)
admin.site.register(QuestionPaper)

## For exam management ##
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(CourseV2)
admin.site.register(SessionV2)
admin.site.register(SubjectV2)
admin.site.register(Subject_Semester)
admin.site.register(Exam_Type)
admin.site.register(Faculty_Designation)
admin.site.register(Faculty)
admin.site.register(Exam)
admin.site.register(Student_Marks)
admin.site.register(Faculty_Subjects)
