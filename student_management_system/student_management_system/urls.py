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

                  # Staff
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

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
