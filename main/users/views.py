from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib .auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created ! You may log In')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html' , {'form':form}) 

@login_required
def profile(request):
    return render( request , 'users/profile.html' )