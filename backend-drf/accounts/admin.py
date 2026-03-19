from django.contrib import admin
from .models import User
# Register your models here.

# admin user manager
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','username','is_staff','is_active','is_superuser')
    list_filter = ('email','is_staff','is_active','is_superuser')
admin.site.register(User)
