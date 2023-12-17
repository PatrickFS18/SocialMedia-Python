from django.urls import path
from .views import login_home

app_name = 'login'  

urlpatterns = [
    path('', login_home, name='login'),
]
