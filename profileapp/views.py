from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from modelsapp.models import UserProfileInfo

@login_required(login_url='loginsignapp:login')
def home(request):
    current_user_profile = UserProfileInfo.objects.get(user=request.user)
    current_user = request.user

    context = {'current_user_profile':current_user_profile, 'current_user':current_user}
    if request.method == 'POST':
        if '_user' in request.POST:
            temp_user = request.user
            temp_user.username = request.POST.get('username')
            temp_user.email = request.POST.get('email')
            temp_user.first_name = request.POST.get('first_name')
            temp_user.last_name = request.POST.get('last_name')
            temp_user.save()

            
    return render (request, 'userprofile/user-profile.html', context)    