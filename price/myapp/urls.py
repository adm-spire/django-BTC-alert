# myapp/urls.py
from django.urls import path
from .views import create_alert, delete_alert, fetch_alerts, process_alerts
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('alerts/create/', create_alert, name='create_alert'),
    path('alerts/delete/<int:pk>/', delete_alert, name='delete_alert'),
    path('alerts/fetch/', fetch_alerts, name='fetch_alerts'),
    path('alerts/process/', process_alerts, name='process_alerts'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
