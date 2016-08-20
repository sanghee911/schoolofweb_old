from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'profiles'
    verbose_name = 'profile'
    template = 'account/stacked.html'
    exclude = ('full_name',)


# Define a new User admin
class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)

    def save_model(self, request, obj, form, change):
        user_profile = obj.profile
        user_profile.save()
        obj.save()

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
