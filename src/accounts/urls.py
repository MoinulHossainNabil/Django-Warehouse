from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (UserView,
                    UserDetail,
                    MyTokenObtainPairView,
                    confirm_user_by_email)


urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('send_mail/', confirm_user_by_email.as_view(), name="email-confirm")
]
