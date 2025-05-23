from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("last_name", "first_name", "email")
    list_display = ("email", "last_name", "first_name")
    readonly_fields = ("last_login", "password", "date_joined")
    #
    # def get_fields(self, request, obj = None):
    #     fieldsets = super().get_fields(request, obj)
    #
    #     return tuple(
    #         (name, {'fields': [f for f in opts['fields'] if f != 'password']})
    #         for name, opts in fieldsets
    #     )
