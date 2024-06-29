from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UploadMedia
from .forms import UploadForm

import os 
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render (request, 'login.html')

# @login_required(login_url='/login')   
def index(request):
   # try:
    return render(request, 'index.html')
    # except:
    #      return HttpResponse({'msg':'server is upgrading'})

@login_required(login_url='/login')
def UploadImgGallery(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_media = UploadMedia(upload_user=request.user, img_bio=form.cleaned_data['img_bio'])
            upload_media.save()  # Save to get an ID

            # Handle file uploads
            files = request.FILES.getlist('img')
            image_paths = []

            for file in files:
                filename = file.name
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                
                # Save file to MEDIA_ROOT
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                # Append relative path for storage in JSONField
                relative_path = os.path.join(settings.MEDIA_URL, filename)
                image_paths.append(relative_path)

            # Save image paths to JSONField
            upload_media.images = image_paths
            upload_media.save()

            return redirect('index')  # Redirect after successful upload
    else:
        form = UploadForm()

    return render(request, 'upload_gallery.html', {'form': form})

def get_gallery_data(request):
    data = UploadMedia.objects.all()
    return render(request, 'get_gallery.html', {'data': data})


