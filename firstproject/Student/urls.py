from django.urls import path
from . import views

urlpatterns =[
    path('dashboard',views.dashboard,name='student'),
    path('dashboard',views.dashboard,name='student'),
    path('stu_profile',views.stu_profile,name ='stu_profile'),

]