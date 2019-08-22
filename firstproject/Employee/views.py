from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'employee/dashboard.html')


def employeefill(request):
    return render(request,'employee/employee_fill.html')
