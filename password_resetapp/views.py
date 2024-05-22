from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site


def reset_password(request):
    
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            current_site = get_current_site(request)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password reset Requested"
                    email_template_name = "passwordReset/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': current_site.domain,
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request,
                                     'Check your inbox, We have Emailed you the instructions to reset your Password')
                    return redirect("loginsignapp:login")
    password_reset_form = PasswordResetForm()
    return render(request,'passwordReset/password_reset.html', context={"password_reset_form": password_reset_form})
