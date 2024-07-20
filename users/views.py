from django.shortcuts import get_object_or_404, redirect, render 
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cms.forms import DonationForm
from cms.models import DonatedPerson, DonationCategory 
from .models import User 
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout


def createuser(request):  
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():  
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('login')  # Redirect to login page or another success page
        else:
            print(form.errors)
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form': form  
    }  
    return render(request, 'create-user.html', context)

def LoginView(request):
    if request.method == 'POST':  
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['user_type'] = user.user_type
            # Redirect based on next parameter or user type
            if user.user_type == 'adminuser':
                return redirect('dashboard')
            elif user.user_type == 'Donor':
                return redirect('/')
            # else:
            #     return redirect('default_dashboard')

        else:
            # Password does not match or user does not exist
            messages.error(request,"Username or password not correct")
    return render(request, 'login.html')


def LogoutView(request):
    logout(request)
    return redirect('login')


#Donation 
@login_required(login_url='/login')
def donate(request, category_id):
    category = get_object_or_404(DonationCategory, id=category_id)
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            amount_paid = form.cleaned_data['amount_paid']
            custom_amount_paid = form.cleaned_data['custom_amount_paid']
            request_80g = form.cleaned_data['request_80g']

            # Create user with phone number as password
            user = User.objects.create_user(
                username=username,
                email=email,
                password=mobile,  # Using phone number as password
            )

            # Store donation details
            donation = DonatedPerson.objects.create(
                user=user,
                amount_paid=amount_paid,
                custome_amount_paid=custom_amount_paid,
                request_80g=request_80g,
                donate_category=category
            )
            print("donation save",donation)

            return JsonResponse({'success': True})

        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = DonationForm()
        
    return render(request, 'index.html', {'form': form, 'category': category})