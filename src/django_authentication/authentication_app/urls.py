from django.contrib import admin
from django.urls import path, include
from .views import LoginView, SignupView, LogoutView

app_name = 'authentication_app'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
