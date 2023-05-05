
from django.contrib import admin
from django.urls import path
# Below 2 namespaces are added by me

from django.conf import settings
from django.conf.urls .static import static

from .import views,hod_views,staff_views,student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('login/', views.LOGIN, name='login'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
