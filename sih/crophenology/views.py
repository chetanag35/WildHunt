from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def dashboard(request):
    if request.user.is_authenticated:
        username=request.user.username
        return render(request, 'dashboard.html', {'username':username,})
    else:
        error="not signed in"
        return render(request, 'myprofile.html', {'error':error,})

def upload_data(request):
    if request.method == "POST":
        folder_path = request.POST.get('textfield', None)
        return HttpResponseRedirect('/user/dashboard')
    else:
        return render(request,'upload.html')