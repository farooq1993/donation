from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os 
from django.conf import settings

from cms.models import *
from .models import UploadMedia
from .forms import UploadForm

 
def index(request):
    try:
        #calling Hero section data
        data = HeroSectionContent.objects.first()
        donate_data = DonationCard.objects.get()
        return render(request, 'index.html', {'data':data,'donate_data':donate_data})
    except:
         return JsonResponse({'msg':'server is upgrading'})

@login_required(login_url='/users/login')
def UploadImgGallery(request):
    user = request.user
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
            messages.success(request ,"Images uploaded successfully")
            return redirect('index')  # Redirect after successful upload
    else:
        form = UploadForm()

    return render(request, 'upload_gallery.html', {'form': form, 'user':user})

# def get_gallery_data(request):
#     data = UploadMedia.objects.all()
#     return render(request, 'get_gallery.html', {'data': data})


#show our work 
def our_work(request):
    try:
        return render(request, 'our-work.html')
    except:
        return JsonResponse({"msg":"page not found"})


#Trustee
def trustee(request):
    try:
        return render(request, 'trustees.html')
    except:
        return JsonResponse({"msg":"page not found"})
    
#about
def about(request):
    try:
        return render(request, 'about.html')
    except:
        return JsonResponse({"msg":"page not found"})

#Gallery
def gallery(request):
    try:
        data = UploadMedia.objects.all()
        return render(request, 'gallery.html',{"data":data})
    except:
        return JsonResponse({"msg":"page not found"})
    
#Get involved
def get_involved(request):
    try:
        return render(request, 'csr.html')
    except:
        return JsonResponse({"msg":"page not found"})


