from django.contrib import admin
from django.urls import path, include
from .views import home, AddPerson, UpdatePerson, delete_person,PersonList, get_city_by_country_id, autocomplete

app_name = 'base_app'

urlpatterns = [
    path('', home, name="home"),
    path('add-person/', AddPerson.as_view(), name='add-person'),
    path('update-person/<int:pk>/', UpdatePerson.as_view(), name='update-person'),
    path('delete-person/<int:pk>/', delete_person, name='delete-person'),
    path('person-list/', PersonList.as_view(), name='person-list'),
    path('country-cities/<int:pk>/', get_city_by_country_id, name='country-cities'),
    path('autocomplete/', autocomplete, name='autocomplete'),
]
