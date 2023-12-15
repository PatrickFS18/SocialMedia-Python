from django.urls import path
from .views import CustomLoginView, login_view

app_name = 'login'  

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]
