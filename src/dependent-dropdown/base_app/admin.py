from django.contrib import admin
from .models import UserProfile, Country, City, Person


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
    list_display = ['__str__', 'address', 'country']


class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Person
    list_display = ['__str__', 'city', 'country']

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person, PersonAdmin)
