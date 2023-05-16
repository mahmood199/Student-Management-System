from django.contrib import admin
from django.urls import path
# Below 2 namespaces are added by me

from django.conf import settings
from django.conf.urls.static import static

from . import views, hod_views, staff_views, student_views


class hod_Views:
    pass


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),

                  # Login Path
                  path('', views.LOGIN, name='login'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),

                  # Profile Update
                  path('Profile', views.PROFILE, name='profile'),
                  path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  # HOD Panel URL
                  path('Hod/Home', hod_views.HOME, name='hod_home'),
                  path('Hod/Student/Add', hod_views.ADD_STUDENT, name='add_student'),
                  path('Hod/Student/View', hod_views.VIEW_STUDENT, name='view_student'),
                  path('Hod/Student/Edit/<str:id>', hod_views.EDIT_STUDENT, name='edit_student'),
                  path('Hod/Student/Update', hod_views.UPDATE_STUDENT, name='update_student'),
                  path('Hod/Student/Delete/<str:admin>', hod_views.DELETE_STUDENT, name='delete_student'),

                  path('Hod/Course/Add', hod_views.ADD_COURSE, name='add_course'),
                  path('Hod/Course/View', hod_views.VIEW_COURSE, name='view_course'),
                  path('Hod/Course/Edit/<str:id>', hod_views.EDIT_COURSE, name='edit_course'),
                  path('Hod/Course/Update', hod_views.UPDATE_COURSE, name='update_course'),
                  path('Hod/Course/Delete/<str:id>', hod_views.DELETE_COURSE, name='delete_course'),

                  path("Hod/Staff/Add", hod_views.ADD_STAFF, name="add_staff"),
                  path("Hod/Staff/View", hod_views.VIEW_STAFF, name="view_staff"),
                  path("Hod/Staff/Edit/<str:id>", hod_views.EDIT_STAFF, name="edit_staff"),
                  path("Hod/Staff/Update", hod_views.UPDATE_STAFF, name="update_staff"),
                  path("Hod/Staff/Delete/<str:admin>", hod_views.DELETE_STAFF, name="delete_staff"),

                  path("Hod/Subject/Add", hod_views.ADD_SUBJECT, name="add_subject"),
                  path("Hod/Subject/View", hod_views.VIEW_SUBJECT, name="view_subject"),
                  path("Hod/Subject/Edit/<str:id>", hod_views.EDIT_SUBJECT, name="edit_subject"),
                  path("Hod/Subject/Update", hod_views.UPDATE_SUBJECT, name="update_subject"),
                  path("Hod/Subject/Delete/<str:id>", hod_views.DELETE_SUBJECT, name="delete_subject"),

                  path("Hod/Session/Add", hod_views.ADD_SESSION, name="add_session"),
                  path("Hod/Session/View", hod_views.VIEW_SESSION, name="view_session"),
                  path("Hod/Session/Edit/<str:id>", hod_views.EDIT_SESSION, name="edit_session"),
                  path("Hod/Session/Update", hod_views.UPDATE_SESSION, name="update_session"),
                  path("Hod/Session/Delete/<str:id>", hod_views.DELETE_SESSION, name="delete_session"),

                  path('Hod/Staff/Send_Notification', hod_views.STAFF_SEND_NOTIFICATION,
                       name='staff_send_notification'),

                  path('Hod/Staff/save_notification', hod_views.SAVE_STAFF_NOTIFICATION,
                       name='save_staff_notification'),

                  path('Hod/Student/send_notification', hod_views.STUDENT_SEND_NOTIFICATION,
                       name='student_send_notification'),
                  path('Hod/Student/save_notification', hod_views.SAVE_STUDENT_NOTIFICATION,
                       name='save_student_notification'),

                  path('Hod/Staff/Leave_view', hod_views.Staff_Leave_view, name='staff_leave_view'),
                  path('Hod/Staff/approve_leave/<str:id>', hod_views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
                  path('Hod/Staff/disapprove_leave/<str:id>', hod_views.STAFF_DISAPPROVE_LEAVE,
                       name='staff_disapprove_leave'),


                  path('Hod/Staff/feedback', hod_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
                  path('Hod/Staff/feedback/save', hod_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),


                  path('Hod/Student/leave_view', hod_views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
                  path('Hod/Student/approve_leave/<str:id>', hod_views.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
                  path('Hod/Student/disapprove_leave/<str:id>', hod_views.STUDENT_DISAPPROVE_LEAVE,
                       name='student_disapprove_leave'),

                  path('Hod/Student/feedback', hod_views.STUDENT_FEEDBACK, name='get_student_feedback'),
                  path('Hod/Student/feedback/reply/save', hod_views.REPLY_STUDENT_FEEDBACK, name='reply_student_feedback'),
                  path('Hod/View/Attendance', hod_views.VIEW_ATTENDANCE, name='view_attendance'),

                  # Staff
                  path("staff/home", staff_views.HOME, name="staff_home"),

                  path('staff/notifications', staff_views.NOTIFICATIONS, name='notifications'),
                  path('staff/mark_as_done/<str:status', staff_views.STAFF_NOTIFICATION_MARK_AS_DONE,
                       name='staff_notification_mark_as_done'),

                  path('staff/Apply_leave', staff_views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
                  path('staff/Apply_leave_save', staff_views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),
                  path('staff/Feedback', staff_views.STAFF_FEEDBACK, name='staff_feedback'),
                  path('staff/Feedback/Save', staff_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),
                  path('staff/Take_Attendance', staff_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
                  path('staff/Save_Attendance', staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
                  path('staff/View_Attendance', staff_views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

                  # Student urls

                  path('Student/Home', student_views.Home, name='student_home'),

                  path('Student/Notifications', student_views.STUDENT_NOTIFICATION, name='student_notification'),
                  path('Student/mark_as_done/<str:status', student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,
                       name='student_notification_mark_as_done'),

                  path('Student/feedback', student_views.STUDENT_FEEDBACK, name='student_feedback'),
                  path('Student/feedback/save', student_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),


                  path('Student/apply_for_leave', student_views.STUDENT_LEAVE, name='student_leave'),
                  path('Student/Leave_save', student_views.STUDENT_LEAVE_SAVE, name='student_leave_save'),

                  path('Student/View_attendance', student_views.VIEW_ATTENDANCE, name='student_view_attendance'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
