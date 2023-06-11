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
                  path('hod/home', hod_views.HOME, name='hod_home'),
                  path('hod/profile', hod_views.PROFILE, name='hod_profile'),

                  path('hod/student/Add', hod_views.ADD_STUDENT, name='add_student'),
                  path('hod/student/View', hod_views.VIEW_STUDENT, name='view_student'),
                  path('hod/student/Edit/<str:id>', hod_views.EDIT_STUDENT, name='edit_student'),
                  path('hod/student/Update', hod_views.UPDATE_STUDENT, name='update_student'),
                  path('hod/student/Delete/<str:admin>', hod_views.DELETE_STUDENT, name='delete_student'),

                  path("hod/staff/Add", hod_views.ADD_STAFF, name="add_staff"),
                  path("hod/staff/View", hod_views.VIEW_STAFF, name="view_staff"),
                  path("hod/staff/Edit/<str:id>", hod_views.EDIT_STAFF, name="edit_staff"),
                  path("hod/staff/Update", hod_views.UPDATE_STAFF, name="update_staff"),
                  path("hod/staff/Delete/<str:admin>", hod_views.DELETE_STAFF, name="delete_staff"),

                  path("hod/session/Add", hod_views.ADD_SESSION, name="add_session"),
                  path("hod/session/View", hod_views.VIEW_SESSION, name="view_session"),
                  path("hod/session/Edit/<str:id>", hod_views.EDIT_SESSION, name="edit_session"),
                  path("hod/session/Update", hod_views.UPDATE_SESSION, name="update_session"),
                  path("hod/session/Delete/<str:id>", hod_views.DELETE_SESSION, name="delete_session"),

                  path('hod/staff/Send_Notification', hod_views.STAFF_SEND_NOTIFICATION,
                       name='staff_send_notification'),

                  path('hod/staff/save_notification', hod_views.SAVE_STAFF_NOTIFICATION,
                       name='save_staff_notification'),

                  path('hod/student/send_notification', hod_views.STUDENT_SEND_NOTIFICATION,
                       name='student_send_notification'),
                  path('Hod/Student/save_notification', hod_views.SAVE_STUDENT_NOTIFICATION,
                       name='save_student_notification'),

                  path('hod/Staff/Leave_view', hod_views.Staff_Leave_view, name='staff_leave_view'),
                  path('hod/Staff/approve_leave/<str:id>', hod_views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
                  path('hod/Staff/disapprove_leave/<str:id>', hod_views.STAFF_DISAPPROVE_LEAVE,
                       name='staff_disapprove_leave'),

                  path('hod/Staff/feedback', hod_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
                  path('hod/Staff/feedback/save', hod_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),

                  path('hod/Student/leave_view', hod_views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
                  path('hod/Student/approve_leave/<str:id>', hod_views.STUDENT_APPROVE_LEAVE,
                       name='student_approve_leave'),
                  path('hod/Student/disapprove_leave/<str:id>', hod_views.STUDENT_DISAPPROVE_LEAVE,
                       name='student_disapprove_leave'),

                  path('hod/Student/feedback', hod_views.STUDENT_FEEDBACK, name='get_student_feedback'),
                  path('hod/Student/feedback/reply/save', hod_views.REPLY_STUDENT_FEEDBACK,
                       name='reply_student_feedback'),


                  path('hod/assign_exam_roles', hod_views.ASSIGN_EXAM_ROLE, name='assign_exam_roles'),
                  path('hod/view_all_exam_roles', hod_views.VIEW_ALL_EXAM_ROLES, name='view_all_exam_roles'),



                  path('hod/add_subject_semester', hod_views.ADD_SUBJECT_SEMESTER, name='add_subject_semester'),
                  path('hod/view_subject_semester', hod_views.VIEW_SUBJECT_SEMESTER, name='view_subject_semester'),
                  path('hod/add_faculty_subject_semester', hod_views.ADD_FACULTY_SUBJECT_SEMESTER,
                       name='add_faculty_subject_semester'),
                  path('hod/view_faculty_subject_semester', hod_views.VIEW_FACULTY_SUBJECT_SEMESTER,
                       name='view_faculty_subject_semester'),

                  ## Semesters
                  path('hod/add_semester', hod_views.ADD_SEMESTER, name='add_semester'),
                  path('hod/edit_semester/<str:id>', hod_views.EDIT_SEMESTER, name='edit_semester'),
                  path('hod/view_semester', hod_views.VIEW_SEMESTER, name='view_semester'),
                  path("hod/semester/Update", hod_views.UPDATE_SEMESTER, name="update_semester"),

                  path('hod/add_department', hod_views.ADD_DEPARTMENT, name='add_department'),
                  path('hod/view_department', hod_views.VIEW_DEPARTMENT, name='view_department'),

                  path('hod/add_exam_type', hod_views.ADD_EXAM_TYPE, name='add_exam_type'),
                  path('hod/view_exam_type', hod_views.VIEW_EXAM_TYPES, name='view_exam_types'),

                  path('hod/add_session_v2', hod_views.ADD_SESSION_V2, name='add_session_v2'),
                  path('hod/view_session_v2', hod_views.VIEW_SESSION_V2, name='view_session_v2'),

                  path('hod/course/View', hod_views.VIEW_COURSE, name='view_course_v2'),
                  path('hod/add_course_v2', hod_views.ADD_COURSE_V2, name='add_course_v2'),
                  path('hod/course/Edit/<str:id>', hod_views.EDIT_COURSE, name='edit_course'),
                  path('hod/course/Update', hod_views.UPDATE_COURSE, name='update_course'),

                  path('hod/add_subject_v2', hod_views.ADD_SUBJECT_V2, name='add_subject_v2'),
                  path('hod/view_subject_v2', hod_views.VIEW_SUBJECT_V2, name='view_subject_v2'),
                  path("hod/edit_subject_v2/<str:id>", hod_views.EDIT_SUBJECT, name="edit_subject"),
                  path("hod/update_subject_v2", hod_views.UPDATE_SUBJECT, name="update_subject"),
                  path("hod/delete_subject_v2/<str:id>", hod_views.DELETE_SUBJECT, name="delete_subject"),

                  path('hod/add_faculty_designation', hod_views.ADD_FACULTY_DESIGNATIONS,
                       name='add_faculty_designation'),
                  path('hod/view_faculty_designations', hod_views.VIEW_FACULTY_DESIGNATIONS,
                       name='view_faculty_designations'),

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
                  path('staff/Add/Result', staff_views.STAFF_ADD_RESULT, name='staff_add_result'),
                  path('staff/Save/Result', staff_views.STAFF_SAVE_RESULT, name='staff_save_result'),

                  # Question Papers
                  path('staff/add_question_paper', staff_views.STAFF_ADD_QUESTION_PAPER,
                       name='staff_add_question_paper'),

                  path('staff/view_all_question_papers', staff_views.VIEW_ALL_QUESTION_PAPERS,
                       name='staff_view_all_question_papers'),

                  path('staff/edit_question_paper/<str:id>', staff_views.EDIT_QUESTION_PAPER,
                       name='staff_edit_question_paper'),

                  path('staff/update_question_paper', staff_views.UPDATE_QUESTION_PAPER,
                       name='staff_update_question_paper'),

                  path('staff/review_question_paper/<str:id>', staff_views.REVIEW_QUESTION_PAPER,
                       name='staff_review_question_paper'),

                  path('staff/add_comments_on_question_paper', staff_views.ADD_COMMENTS_ON_QUESTION_PAPER,
                       name='staff_add_comments_on_question_paper'),

                  path('staff/approve_question_paper/<str:id>', staff_views.APPROVE_QUESTION_PAPER,
                       name='staff_approve_question_paper'),

                  path('staff/view_question_paper/<str:id>', staff_views.VIEW_ALL_QUESTION_PAPER,
                       name='staff_view_question_paper'),

                  path('staff/view_question_paper_pdf/<str:id>', staff_views.DOWNLOAD_QUESTION_PAPER_PDF,
                       name='staff_view_question_paper_pdf'),
                  # setter url
                  path('staff/staff_setter', staff_views.STAFF_SETTER, name='staff_setter'),
                  # moderator url
                  path('staff/staff_moderator', staff_views.STAFF_MODERATOR, name='staff_moderator'),

                  path('staff/staff_examiner', staff_views.STAFF_EXAMINER, name='staff_examiner'),

                  path('staff/staff_scrutinizer', staff_views.STAFF_SCRUTINIZER, name='staff_scrutinizer'),

                  path('staff/staff_head_examiner', staff_views.STAFF_HEAD_EXAMINER,
                       name='staff_head_examiner'),

                    #roles that is assigned to loggedin staff
                  path('staff/view_my_exam_roles', staff_views.VIEW_MY_EXAM_ROLES, name='view_my_exam_roles'),


                  path('staff/question_paper_setter/<str:id>', staff_views.SETTER_ADD_QUESTION_PAPER, name='setter_add_question_paper'),
                  path('staff/question_paper_moderator/<str:id>', staff_views.MODERATOR_ADD_QUESTION_PAPER, name='moderator_add_question_paper'),
                  path('staff/view_exam_question_paper/<str:id>', staff_views.VIEW_QUESTION_PAPER, name='view_exam_question_paper'),



                  # Student urls

                  path('student/Home', student_views.Home, name='student_home'),

                  path('student/Notifications', student_views.STUDENT_NOTIFICATION, name='student_notification'),
                  path('student/mark_as_done/<str:status', student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,
                       name='student_notification_mark_as_done'),

                  path('student/feedback', student_views.STUDENT_FEEDBACK, name='student_feedback'),
                  path('student/feedback/save', student_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),

                  path('student/apply_for_leave', student_views.STUDENT_LEAVE, name='student_leave'),
                  path('student/Leave_save', student_views.STUDENT_LEAVE_SAVE, name='student_leave_save'),

                  path('student/View_attendance', student_views.VIEW_ATTENDANCE, name='student_view_attendance'),
                  path('student/view_result', student_views.VIEW_RESULT, name='view_result'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
