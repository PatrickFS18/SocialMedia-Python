from django.urls import path
from .views import CustomLoginView

app_name = 'login'  

urlpatterns = [
    path('login/', CustomLoginView, name='login'),
]