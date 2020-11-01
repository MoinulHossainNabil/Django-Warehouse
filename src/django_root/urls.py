from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Api Documentation View')

urlpatterns = [
    path('api-documentation-view/', schema_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('base_app/', include('base_app.urls')),

]
