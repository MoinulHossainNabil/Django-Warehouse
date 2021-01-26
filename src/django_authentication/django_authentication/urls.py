from django.contrib import admin
from django.urls import path, include
from authentication_app.views import Home
from django.contrib.auth import views as auth_views
from authentication_app.forms import EmailValidationOnResetPassword
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication_app.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=EmailValidationOnResetPassword), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
