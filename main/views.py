from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PreviousJob

# Create your views here.
def landing_page(request):
    user = User.objects.all()
    context = {
        "users": user,
        "jobs": PreviousJob.objects.all()
    }
    return render(request, "main/landing.html",context)   