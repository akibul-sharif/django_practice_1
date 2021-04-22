from django.shortcuts import render
from .models import Profile


# Create your views here.

def profile_homepage(request):
    profile=Profile.objects.all()
    context={
        'profile':profile

    }
    return render(request,'index.html',context)
