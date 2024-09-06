from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .form import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from job.views import job_list

app_name="accounts"
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data['phone_number']
            image = form.cleaned_data['image']
            city = form.cleaned_data['city']

            Profile.objects.update_or_create(
                user=user,
                defaults={
                    'phone_number': phone_number,
                    'image': image,
                    'city':city
                }
            )
            
            # Authenticate and log in the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{"profile":profile})
@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect('accounts:profile')  # Redirect to the profile page or wherever appropriate
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    
    context = {
        "userform": userform,
        "profileform": profileform
    }
    return render(request, 'accounts/profile_edit.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')  