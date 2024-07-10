from django.shortcuts import redirect, render  
from django.contrib import messages  
from .forms import CustomUserCreationForm 
from django.contrib.auth import login, authenticate 
 
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