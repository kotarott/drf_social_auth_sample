from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from firebase_auth.models import Profile
from firebase_auth.api.serializers import ProfileSerializer
# from firebase_auth.api.permissions import IsOwnProfileOrReadOnly


class ProfileRUAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]
