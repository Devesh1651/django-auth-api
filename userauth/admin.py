from django.contrib import admin
from .models import User, EmailAccount
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active', 'is_verified')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('user_type', 'is_active', 'is_verified')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Verification', {'fields': ('is_verified',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'user_type', 'password1', 'password2'),
        }),
    )


class EmailAccountAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'username', 'user', 'is_verified')
    search_fields = ('email', 'username')
    list_filter = ('is_verified',)

    def get_email(self, obj):
        return obj.email or obj.user.email
    get_email.short_description = 'Email'


admin.site.register(User, UserAdmin)
admin.site.register(EmailAccount, EmailAccountAdmin)
