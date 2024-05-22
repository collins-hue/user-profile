from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from userprofile import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profileapp.urls', namespace='profileapp')),
    path('', include('loginsignapp.urls', namespace='loginsignapp')),
    path('', include('password_resetapp.urls', namespace='password_resetapp')),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='passwordReset/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordReset/password_reset_complete.html'), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)