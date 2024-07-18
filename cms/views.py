from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import os 
import logging
from django.conf import settings
# from django.contrib.auth import get_user_model

# User=get_user_model()


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

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            amount_paid = form.cleaned_data['amount_paid']
            custom_amount_paid = form.cleaned_data['custom_amount_paid']
            request_80g = form.cleaned_data['request_80g']
            category = form.cleaned_data['category']

            # Set the phone number as the user's password
            user = User.objects.create_user(
                username=username,
                email=email,
                mobile=mobile,
                password=mobile,  # Using phone number as password
                user_type='Donor'
            )

            # Store donation details
            DonatedPerson.objects.create(
                user=user,
                amount_paid=amount_paid,
                custome_amount_paid=custom_amount_paid,
                request_80g=request_80g
            )

            # Automatically log the user in
            login(request, user)

            return redirect('success_page')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})




    