from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import HeroSectionContent
from .forms import HerosectionForm
import os 
from django.conf import settings


@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/login')
def herosection(request):
    if request.method == 'POST':   
        form = HerosectionForm(request.POST, request.FILES)
        if form.is_valid():
            upload_media = HeroSectionContent(user=request.user, title=form.cleaned_data['title'])
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
            return redirect('dashboard')  # Redirect after successful upload
    # else:
    #     form = HerosectionForm()

    return render(request, 'herosection.html')