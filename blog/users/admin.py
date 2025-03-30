from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("last_name", "first_name", "email")
    list_display = ("email", "first_name", "last_name")
    readonly_fields = ("last_login", "password", "date_joined")

    # Czy da się ukryć hasło z widoku użytkownika??? <- do sprawdzenia ;)
