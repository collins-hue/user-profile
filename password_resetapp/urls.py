from django.urls import path
from password_resetapp import views

app_name = 'password_resetapp'
urlpatterns = [
    path('password_reset/',views.reset_password, name='password_reset'),
]
