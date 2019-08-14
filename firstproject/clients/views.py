from django.shortcuts import render,redirect
from django.contrib import messages,auth
from.models import Client
from .models import PostJob
from django.contrib.auth.models import User


def client_dashboard(request):
    if request.method == 'POST':
        country = request.POST['country']
        mobile = request.POST['mobile']
        department = request.POST['department']
        role = request.POST['role']
        compname = request.POST['name']
        photo = request.POST['pic']

        if Client.objects.filter(phone=mobile).exists():
            messages.error(request, "Mobile number already exists")
            return redirect('clients')
        else:
            user = request.user
            pk = user.id
            var = Client(client_id=pk, country=country, phone=mobile, department=department, role=role, name=compname,
                         photo=photo)
            var.save()
            messages.success(request,'Submitted successfully')
            return redirect('client_main')
    else:
        # IF FAILURE
        return render(request,'clients/client_dashboard.html')




def client_main(request):
    if request.method == 'POST':
        jobtitle = request.POST['JobTitle']
        jobtype = request.POST['JobType']
        jobcategory = request.POST['JobCategory']
        location = request.POST['location']
        salary = request.POST['Salary']
        tags = request.POST['tags']
        jobdescription = request.POST['JobDescription']
        client = request.user
        c_id = client.id
        var = PostJob(client_id=c_id, jobtitle=jobtitle, jobtype=jobtype, jobcategory=jobcategory, location=location,
                      salary=salary, tags=tags, jobdescription=jobdescription)
        var.save()
        messages.success(request, "Submitted Successfuly")
        return redirect('client_main')
    else:
        messages.error(request,"not found")
    return render(request, 'clients/client_main.html')

def client_settings(request):
    return render(request, 'clients/client_settings.html')














# Create your views here.
