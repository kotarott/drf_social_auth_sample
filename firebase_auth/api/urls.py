from django.urls import path, include
from firebase_auth.api.views import ProfileRUAPIView

urlpatterns = [
    path('<int:pk>/', ProfileRUAPIView.as_view(), name='profile-detail')
]