from django.urls import path
from .views import register_view

app_name = 'register'

urlpatterns = [
    path('', register_view, name='register'),
]