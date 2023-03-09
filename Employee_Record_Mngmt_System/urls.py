"""Employee_Record_Mngmt_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Employee_RMS import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name ="home"),
    path('home1/', views.Home,name ="home1"),
    path('registration/', views.registration,name = "registration"),
    path('employee_login/', views.employee_login,name = "employee_login"),
    path('employee_home/', views.employee_home,name = "employee home"),
    path('profile/', views.employee_profile,name = "profile"),
    path('logout/', views.Logout,name ="logout"),
    path('admin_login/', views.admin_login,name ="admin_login"),
    path('experience/', views.employee_experience,name ="experience"),
    path('edit_experience/', views.edit_experience,name ="edit_experience"),
    path('education/', views.employee_education,name ="education"),
    path('edit_education/', views.edit_education,name ="edit_education"),
    path('change_password/', views.change_password,name ="change_password"),
    path('admin_home/', views.admin_home,name ="admin_home"),
    path('admin_change_pass/', views.admin_change_password,name ="admin_change_pass"),
    path('admin_logout/', views.admin_Logout,name ="admin_logout"),
    path('all_employee/', views.all_employee,name ="all_employee"),
    path('delete_employee/<int:pid>', views.delete_employee,name ="delete_employee"),
    path('edit_employee/<int:pid>', views.edit_employee,name ="edit_employee"),
    path('edit_edu_admin/<int:pid>', views.edit_education_admin,name ="edit_edu_admin"),
    path('edit_exp_admin/<int:pid>', views.edit_experience_admin,name ="edit_exp_admin"),
    path('edit_exp_admin/<int:pid>', views.edit_experience_admin,name ="edit_exp_admin"),
    path('csv-export/',views.CsV_File_Expo,name ="csv"),
    path('results/',views.results,name ="results"),
    path('material/',views.material,name ="material"),
    path('uploadmaterial/',views.uploadmaterial,name ="uploadmaterial"),
    path('uploadresult/',views.uploadresult,name ="uploadresult"),
    path('downloadresult/<int:pid>',views.downloadresult,name ="downloadresult"),
    path('deleteresult/<int:id>',views.deleteresult,name ="deleteresult"),
    path('deletematerial/<int:id>',views.deletematerial,name ="deletematerial"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)