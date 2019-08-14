from django.urls import path
from . import views

urlpatterns =[
    path('client_dashboard', views.client_dashboard,name='clients'),
    path('client_main', views.client_main, name='client_main'),
    path('client_settings',views.client_settings,name= 'client_settings')


]