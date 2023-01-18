from django.contrib import admin
from Apps.user.models import UserProfile, Department

from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions',)
    exclude = ('last_login',)


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Department)
