from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'email_is_confirmed',
        'date_joined',
    )
    filter_horizontal = (
        'user_permissions',
        'groups',
    )
    readonly_fields = (
        'password',
        'email_is_confirmed',
        'date_joined',
    )
