from django.contrib import admin
from .models import UserProfile, MultipleFieldJavascript


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
    list_display = ['__str__', 'address']


admin.site.register(UserProfile, UserAdmin)
admin.site.register(MultipleFieldJavascript)
