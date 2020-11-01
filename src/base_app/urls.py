from django.contrib import admin
from django.urls import path, include
from .views import MultipleFieldView

urlpatterns = [
    path('get_multiple_fields/', MultipleFieldView.as_view(), name="multiple_fields"),
]
