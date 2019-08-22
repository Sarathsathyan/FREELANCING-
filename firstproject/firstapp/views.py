from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile
# Create your views here.
def index(request):
    user = request.user
    pk = user.id
    print(pk)
    data = Profile.objects.filter(u_id=pk)
    if data:
        data = Profile.objects.get(u_id = pk)
        print(data)
        context={
            'role' : data.role,
        }
        print(data.role)
        print(context)
        return render(request, 'pages/index.html', context)
    return render(request,'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
