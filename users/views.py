from django.shortcuts import redirect, render 
from django.urls import reverse
from django.contrib import messages  
from .forms import CustomUserCreationForm, CustomLoginForm
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

    # else:
    #     form = CustomLoginForm()
    return render(request, 'login.html')


def LogoutView(request):
    logout(request)
    return redirect('login')