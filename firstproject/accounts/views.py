from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from accounts.models import  Profile
from django.http import HttpResponse

# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        # birthday = request.POST['birthday']
        password = request.POST['password']
        password2 = request.POST['password2']
        role = request.POST['subject']

        # Check password match
        if password == password2:
            #check user
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username Already Exists")
                return redirect('register')

            else:
                # check email
                if User.objects.filter(email = email).exists():
                    messages.error(request, "Email Already Exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    pk = user._get_pk_val()
                    var = Profile(u_id=pk,role=role,id=pk)
                    var.save()
                    # return HttpResponse('')
                    messages.success(request,"Registered successfully")
                    return redirect('login')

        else:
            messages.error(request, "Passwords do not match");
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            check = Profile.objects.get(u_id=user._get_pk_val())
            if check.role == 1:
                auth.login(request, user)

                return redirect('../student/dashboard')
                messages.success(request, 'Welcome Student')
            else:
                messages.success(request, 'Welcome Employee')
                return redirect('../listings/')

        else:
            messages.error(request,'Invalid inputs')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

