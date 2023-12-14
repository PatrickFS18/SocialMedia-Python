from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'nome', 'is_active', 'is_staff')  # Adicione campos válidos do seu modelo
    list_filter = ('is_active', 'is_staff')  # Adicione campos válidos do seu modelo
    ordering = ('email',)  # Adicione campos válidos do seu modelo
    filter_horizontal = ()  # Adicione campos válidos do seu modelo

admin.site.register(Usuario, CustomUserAdmin)