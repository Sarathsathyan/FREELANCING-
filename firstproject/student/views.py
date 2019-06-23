from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request,'student/dashboard.html')

# Create your views here.
