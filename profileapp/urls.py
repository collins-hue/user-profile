from django.urls import path
from profileapp import views

app_name = 'profileapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('signout', views.signout, name='signout')
]
