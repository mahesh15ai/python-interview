from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login_',login_,name='login_'),
    path('logout',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('reset/',reset_password,name='reset'),
    path('forget_pass',forgot_password,name='forget_pass')
    
]