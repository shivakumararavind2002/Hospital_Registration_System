from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from datetime import date
from django.contrib.auth import authenticate,logout,login
# Create your views here.


def AboutMe(request):
    return render(request,'aboutMe.html')

def Contact(request):
    return render(request,'contact.html')
#for doctors
def Doctorview(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'DoctorView.html',d)
#add doctor
def Doctoradd(request):
    error=""
    if request.method == 'POST':
        n = request.POST['Name']
        m = request.POST['Mobile']
        sp = request.POST['Special']
        
        try:
            Doctor.objects.create(name = n,mobile = m,special = sp)
            error = 'no'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'DoctorAdd.html',d)

# for patients
def patientsView(request):
    if not request.user.is_staff:
        return redirect('login')
    pet = Patient.objects.all()
    p = {'pet':pet}
    return render(request,'patientslist.html',p)
# deleteing patient list
def deletepatient(request,did):
    if not request.user.is_staff:
        return redirect('login')
    delpatient = Patient.objects.get(id = did)
    delpatient.delete()
    return redirect('patientslist')
# Edite Patient
def EditePatient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    edi = Patient.objects.get(id = pid)
    if request.method == 'POST':
        edi.name=request.POST['name']
        edi.gender=request.POST['gender']
        edi.mobile=request.POST['mobile']
        edi.address=request.POST['addr']
        edi.docter_name=request.POST['Dname']
        edi.save()
        return redirect('patientslist',)
    pr={'patients':edi}
    return render(request,'EditePatient.html',pr)

# add patients
def addpatients(request):
    error=""
    if request.method == 'POST':
        pn = request.POST['name']
        pg = request.POST['gender']
        pm = request.POST['Mobile']
        pa = request.POST['Address']
        pd = request.POST['Doctor']
       
        try:
            Patient.objects.create(name = pn,gender = pg,mobile = pm,address = pa ,docter_name = pd)
            error = 'no'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'addpatients.html',d)
#index
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

#for login
def Login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        User = authenticate(username = u,password = p)
        try:
            if User.is_staff:
                login(request,User)
                error = 'no'
            else :
                error = 'yes'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'login.html',d)

#for logout
def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

#for delte doctor
def DleteDoctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    delete = Doctor.objects.get(id = pid)
    delete.delete()
    return redirect('doctorlist')

#appointment view
def About(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    d = Doctor.objects.all().count()
    p = Patient.objects.all().count()
    a = Appointment.objects.all().count()
    dal=Appointment.objects.all()
    toDy=date.today()
    p = {'app':app,'d':d,'p':p,'a':a,'dal':dal,'toDy':toDy}
    return render(request,'about.html',p)

#add appointment
def AddAppointment(request):
    error=""
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        dn = request.POST['doctor']
        pn = request.POST['patient']
        d1 = request.POST['date']
        t1 = request.POST['time']
        doctor = Doctor.objects.filter(name=dn).first()
        patient = Patient.objects.filter(name=pn).first()
        try:
            Appointment.objects.create(doctor = doctor,patient = patient,date1 = d1,time1 = t1 )
            error = 'no'
        except:
            error = 'yes'
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'AddAppointment.html',d)

#delete appiontment
def DeleteApoint(request,aid):
    if not request.user.is_staff:
        return redirect('login')
    delApp = Appointment.objects.get(id = aid)
    delApp.delete()
    return redirect('about')



     