
from django.contrib import admin
from django.urls import path
from loginsignapp import views

app_name = 'loginsignapp'
urlpatterns = [
#    re_path('login', views.login_request, name='login'),
    path('login', views.login_request, name='login'),
    path('signup', views.signup, name='signup'),
    path('finalactivate/<uidb64>/<token>', views.finalactivation, name='finalactivate'),
]
