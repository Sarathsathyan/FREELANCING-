from django.urls import path
from . import views

urlpatterns =[
    path('dashboard',views.dashboard,name='employee'),
    path('employeefill',views.employeefill,name='employeefill'),
]