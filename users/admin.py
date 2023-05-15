from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "telegram_id", "is_staff", "is_active", "currency")
    list_filter = ("email", "telegram_id", "is_staff", "is_active", "currency")
    fieldsets = (
        (None, {"fields": (("email", "telegram_id", "currency"), "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "telegram_id", "password1", "password2", "is_staff", "is_active", "is_verified"
            )}
        ),
    )
    search_fields = ("telegram_id", "email")
    ordering = ("telegram_id", "email")


admin.site.register(User, CustomUserAdmin)
