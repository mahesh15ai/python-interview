from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login_',login_,name='login_'),
    path('logout',logout_,name='logout_'),
    
]