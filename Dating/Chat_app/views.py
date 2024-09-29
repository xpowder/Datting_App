from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    return render(request, 'home.html')






@login_required
def Create_Profile(request):


    try:
        profile.user.userprofile
        messages.waring(request, "You already have a profile, You can update it")
        return redirect('profile_detail', profile_id=profile.id)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == "POST":  
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # to Ensures the user is authenticated
            profile.save()
            messages.success(request, "Your profile has been created successfully!") 
            return redirect('discover')
        else:
            messages.error(request, "Please fix the error below")

    else:
        form = UserProfileForm()

    return render(request, 'profile.html', {'form': form})


def Profile_list(request):
    profiles = UserProfile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {'profiles' : profiles})




def Like_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    LikeDislike.objects.update_or_create(
        user_from=request.user,
        user_to=profile.user,
        defaults={'is_like': True}
    )

    return redirect ('discover')


def Dislike_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    LikeDislike.objects.update_or_create(
        user_from=request.user,
        user_to=profile.user,
        defaults={'is_like': False}
    )

    return redirect('discover') 


def profile_like_list(request):
    liked_users = LikeDislike.objects.filter(user_from=request.user, is_like=True).values_list('user_to', flat=True)
    
    profiles = UserProfile.objects.filter(user__in=liked_users)

    return render(request, 'liked_profile.html', {'profiles': profiles})