from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UploadMedia
import logging
# Create your views here.


def LoginView(request):
    return render (request, 'login.html')

#@login_required(login_url='/login')   
def index(request):
    #try:
    return render(request, 'index.html')
    # except:
    #     return HttpResponse({'msg':'server is upgrading'})

#@login_required(login_url='/login')
def UploadImgGallery(request):
    return render(request, 'upload_gallery.html')



