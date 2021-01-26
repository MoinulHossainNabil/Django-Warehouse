from django.urls import path
from .views import UserView, UserDetail

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
]
