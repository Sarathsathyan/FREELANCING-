from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.models import Profile
from django.contrib.auth.models import User
from .models import stupro

# Create your views here.

def dashboard(request):
    return render(request, 'student/dashboard.html')

def stu_profile(request):
    user = request.user
    pk = user.id
    print(pk)
    obj = stupro.objects.filter(stu_id=pk)
    if obj:
        obj = stupro.objects.get(stu_id=pk)
        context = {
            'place': obj.place,
            'state': obj.state,
            'district': obj.district,
            'pincode': obj.pincode,
            'college': obj.collegename,
            'course': obj.qualification,
            'project': obj.project,
            'description': obj.description,
            'photo': obj.photo,
            'name': obj.nick_name,
            'skills': obj.skills,

        }
        return render(request, 'student/stu_profile.html', context)

    elif request.method == 'POST':

        state = request.POST['state']
        district = request.POST['district']
        place = request.POST['place']
        pincode = request.POST['pincode']
        address = request.POST['address']
        college = request.POST['college']
        course = request.POST['course']
        skill = request.POST['skill']
        description = request.POST['descrip']
        project = request.POST['project']
        nick = request.POST['nick']

        if stupro.objects.filter(nick_name = nick).exists():
            messages.error(request,"nick name exists")
            return redirect('stu_profile')
        else:
            user = request.user
            pk = user.id
            var = stupro(stu_id=pk,nick_name=nick,place=place,district=district,state=state, pincode=pincode,address=address,qualification=course,description=description,
                         skills=skill,project=project,collegename=college,)
            var.save()
            # return HttpResponse('')
            messages.success(request, "submitted successfully")
            return redirect('student')

    else:

        return render(request, 'student/stu_profile.html')

# Stu_profile details....

def dashboard(request):
    user = request.user
    pk = user.id
    print(pk)
    obj = stupro.objects.filter(stu_id=pk)
    if obj:
        obj = stupro.objects.get(stu_id=pk)
        context = {
            'place': obj.place,
            'state': obj.state,
            'district': obj.district,
            'pincode': obj.pincode,
            'college': obj.collegename,
            'course': obj.qualification,
            'project': obj.project,
            'description': obj.description,
            'photo' : obj.photo,
            'name' : obj.nick_name,
            'skills' : obj.skills,

        }
        return render(request, 'student/dashboard.html', context)
    else:
        return render(request, 'student/dashboard.html')





