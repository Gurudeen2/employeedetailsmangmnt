from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
from django.core.paginator import Paginator
from datetime import datetime,timedelta, date


def emp_home(request):
    emps=Emp.objects.all().order_by('-name')

    paginator = Paginator(emps, 5)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"emp/home.html",{'emps':page_obj})


# import subprocess
# >>> proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
# >>> stdout, stderr = proc.communicate('dir c:\\')
# >>> stdout

def search(request):
    emps=Emp.objects.all().order_by('-name')
    if request.method == 'GET':
        search = request.GET['search']
        page_obj = emps.filter(name__icontains=search)
        paginator = Paginator(page_obj, 7)  
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        # request.session['search'] = search

    return render(request,"emp/search.html",{'searches':page_obj})

def view_emp(request, id):
    single_emp = Emp.objects.get(pk=id)

    daterange = date.today() - single_emp.date_startwork 
    accuratedate = 0

    if daterange == 30:
        accuratedate=daterange
    # print(daterange)

    return render(request, 'emp/view_emp.html', {'single_emp':single_emp, 'emp_info':accuratedate})


def add_emp(request):
    if request.method=="POST":

        emp_name=request.POST.get("emp_name")
        emp_gender=request.POST.get("emp_gender")
        emp_age=request.POST.get("emp_age")
        emp_religion=request.POST.get("emp_religion")
        emp_phone=request.POST.get("emp_phone")
        emp_qualification=request.POST.get("emp_qualification")
        emp_experience=request.POST.get("emp_experience")
        emp_client=request.POST.get("emp_client")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp()
        e.name=emp_name
        e.age=emp_age
        e.gender=emp_gender
        e.phone=emp_phone
    
        e.department=emp_department
        e.qualification=emp_qualification
        e.religion=emp_religion
        e.client=emp_client
        e.date_startwork=emp_working
    
        e.experience=emp_experience
        e.photo=request.FILES['file']
    

        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })



def do_update_emp(request,id):
    if request.method=="POST":

        
        emp_name=request.POST.get("emp_name")
        emp_gender=request.POST.get("emp_gender")
        emp_age=request.POST.get("emp_age")
        emp_religion=request.POST.get("emp_religion")
        emp_phone=request.POST.get("emp_phone")
        emp_qualification=request.POST.get("emp_qualification")
        emp_experience=request.POST.get("emp_experience")
        emp_client=request.POST.get("emp_client")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        
        Emp.objects.filter(pk=id).update(name=emp_name,
            age=emp_age,
            gender=emp_gender,
            phone=emp_phone,
        
            department=emp_department,
            qualification=emp_qualification,
            religion=emp_religion,
            client=emp_client,
            date_startwork=emp_working,
            experience=emp_experience
        )

        if 'file' in request.FILES:
            Emp.objects.filter(pk=id).update(photo=request.FILES['file'])



      
    return redirect("/emp/home/")
