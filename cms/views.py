from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import os 
import logging
from django.conf import settings



@login_required(login_url='/login')
def dashboard(request):
    user = request.user
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    user_type = request.session.get('user_type')
    logging.info(f"User logged by:{user_type}")
    context = {'user_id': user_id, 'username': username, 'user_type': user_type}
    return render(request, 'dashboard.html', context)

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
            logging.info("Data saved successfully")
            return redirect('dashboard')  # Redirect after successful upload

    return render(request, 'herosection.html')




# Add Donation category
@login_required(login_url='/login')
def add_donation_category(request):
    if request.method == 'POST':
        form = DonationCategoryAdd(request.POST)
        if form.is_valid:
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, "Category Add Successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "Category not saved")

    else:
        form =DonationCategoryAdd()
    return render(request, 'add_category.html')




@login_required(login_url='/login')
def donation_card(request):
    categories = DonationCategory.objects.all()
    
    if request.method == 'POST':
        form = DonationCardForm(request.POST, request.FILES)
        if form.is_valid():
            donation_card = form.save(commit=False)
            donation_card.user = request.user
            category_id = request.POST.get('donate_category')
            if category_id:
                donation_card.donate_category_id = category_id
            donation_card.save()
            messages.success(request, "Donation card added successfully")
            return redirect('dashboard')
        else:
            return JsonResponse({'msg': form.errors})
    else:
        form = DonationCardForm()
    
    return render(request, 'donation_card.html', {'form': form, 'categories': categories})

#Get All Donation Card Data
@login_required(login_url='/login')
def all_donationcards(request):
    donation_card = DonationCard.objects.all().order_by('-id')
    card_list = [card for card in donation_card]
    return render(request, 'all_donation_card.html', {'donation_cards': card_list})

@login_required(login_url='/login')
def get_donationcard(request, id):
    single_donationcard = DonationCard.objects.get(id=id)
    return render(request, 'donate.html', {'single_donationcard':single_donationcard})


