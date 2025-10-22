"""
URL configuration for HospitalRegistrationSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About,name='about'),
    path('aboutMe/',AboutMe,name='aboutMe'),
    path('contact/',Contact,name='contact'),
    path('DoctorList/',Doctorview,name='doctorlist'),
    path('DoctorAdd/',Doctoradd,name='doctorAdd'),
    path('patients/',patientsView,name='patientslist'),
    path('addpatients/',addpatients,name='addpatients'),
    path('edite(?P<int:pid>S)',EditePatient,name='editpatient'),
    path('',Index,name='home'),
    path('admin_login/',Login, name='login'),
    path('logout/',Logout_admin,name='logout'),
    path('DeleteDoctor(?P<int:pid>S)',DleteDoctor,name='deleteDoctor'),
    path('deletepatient(?P<int:did>S)',deletepatient,name='deletePatient'),
    path('addAppoint/',AddAppointment,name='addapointment'),
    path('DelApint(?P<int:aid>S)',DeleteApoint,name='delApoi'),
]
