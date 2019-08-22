from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from.models import Client
from .models import PostJob
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


def client_dashboard(request):
    user = request.user
    pk = user.id
    data = Client.objects.filter(client_id=pk).count()
    if data:
        return redirect('client_main')
    if request.method == 'POST':
        country = request.POST['country']
        mobile = request.POST['mobile']
        department = request.POST['department']
        role = request.POST['role']
        compname = request.POST['name']
        photo = request.POST['pic']

        if Client.objects.filter(phone=mobile).exists():
            messages.error(request,"Mobile number already exists")
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

# client photo
######################################################################################################################

def client_main(request):
    user = request.user
    pk = user.id
    print(pk)
    print("hai")
    obj = Client.objects.filter(client_id=pk)
    if obj:
        obj = Client.objects.get(client_id=pk)
        context={
            'photo': obj.photo,
            'country':obj.country,
        }
        return render(request, 'clients/client_main.html', context)

#######################################################################################################################

def client_main(request):
    user = request.user
    pk = user.id
    print(pk)
    print("hai")
    obj = Client.objects.filter(client_id=pk)
    if obj:
        obj = Client.objects.get(client_id=pk)
        context = {
            'photo': obj.photo,
            'country': obj.country,
        }
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
        print(c_id)
        print("acdc")
        var = PostJob(Id_client=c_id, jobtitle=jobtitle, jobtype=jobtype, jobcategory=jobcategory, location=location,
                      salary=salary, tags=tags, jobdescription=jobdescription)
        var.save()
        messages.success(request, "Submitted Successfuly")
        return redirect('client_main')
    else:
        return render(request, 'clients/client_main.html', context)
    return render(request, 'clients/client_main.html', context)

######################################################################################################################

def client_settings(request):
    user = request.user
    pk = user.id
    print(pk)
    obj = Client.objects.filter(client_id=pk)
    if obj:
        obj = Client.objects.get(client_id=pk)
        context = {
            'photo': obj.photo
        }
        if request.method == "POST":
            form = PasswordChangeForm(request.POST,request.user)
            if form.is_valid():
                form.save()
                return redirect('client_main')

        return render(request, 'clients/client_settings.html', context)
    return render(request, 'clients/client_settings.html')

######################################################################################################################

def client_dash(request):
    user = request.user
    pk = user.id
    print(pk)
    job_count = PostJob.objects.count()
    client_count = Client.objects.count()
    print(job_count)
    obj = Client.objects.filter(client_id=pk)
    if obj:
        obj = Client.objects.get(client_id=pk)
        context = {

            'photo': obj.photo,
            'name': obj.name,
            'job_count':job_count,
            'client_count':client_count
        }

    return render(request, 'clients/client_dash.html',context)

#####################################################################################################################
# Company Profile
def company_profile(request):
    user = request.user
    pk = user.id
    print(pk)
    obj = Client.objects.filter(client_id=pk)
    if obj:
        obj = Client.objects.get(client_id=pk)

        context = {
            'role':obj.role,
            'name': obj.name,
            'dept':obj.department,
            'photo':obj.photo,
            'country':obj.country,
            'about':obj.about_company

        }
        return render(request, 'clients/company_profile.html', context)
    return render(request, 'clients/company_profile.html')




# Create your views here.
