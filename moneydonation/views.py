from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UploadMedia
import logging
# Create your views here.


    
def index(request):
    try:
        return render(request, 'index.html')
    except:
        return HttpResponse("Some issue in Server")

def LoginView(request):
    pass

@login_required(login_url='Loginview')
def UploadImgGallery(request):
    pass



