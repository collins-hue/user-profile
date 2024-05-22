from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loginsignapp.forms import UpdateProfilePic
from modelsapp.models import UserProfileInfo
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
#from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='loginsignapp:login')
def home(request):
    current_user_profile = UserProfileInfo.objects.get(user=request.user)
    current_user = request.user
    context = {'current_user':current_user, 'current_user_profile':current_user_profile}
    print(current_user_profile.profile_picture)
    print(current_user_profile.address)
    print(current_user_profile.city)

    if request.method == 'POST':
        if '_user' in request.POST:
            temp_user = request.user
            temp_user.username = request.POST.get('username')
            temp_user.email = request.POST.get('email')
            temp_user.first_name = request.POST.get('first_name')
            temp_user.last_name = request.POST.get('last_name')
            temp_user.save()

            context = {'current_user':current_user, 'current_user_profie':current_user_profile}
            return redirect ('profileapp:home')
        
        if '_profile' in request.POST:
            temp_user_profile = UserProfileInfo.objects.get(user=request.user)
            temp_user_profile.address = request.POST.get('address')
            temp_user_profile.city = request.POST.get('city')
            temp_user_profile.contact = request.POST.get('contact')
            temp_user_profile.save()

            context = {'current_user':current_user, 'current_user_profile':current_user_profile}
            return redirect ('profileapp:home')
        
        if '_picture' in request.POST:
            form = UpdateProfilePic(request.POST, request.FILES)
            if form.is_valid():
                m = UserProfileInfo.objects.get(user=request.user)
                m.profile_picture = form.cleaned_data['image']
                m.save()
        return redirect ('profileapp:home')

    return render (request, 'userprofile/profile-edit.html', context)

        
@login_required(login_url='loginsignapp:login')
def signout(request):
    request.session.clear()
    return redirect ('loginsignapp:signup')
 #   return HttpResponseRedirect(reverse('loginsignapp:signup'))
