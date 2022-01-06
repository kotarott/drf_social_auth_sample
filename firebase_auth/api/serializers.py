from rest_framework import serializers
from firebase_auth.models import Profile


class ProfileSerializer(serializers.ModelSerialzier):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"