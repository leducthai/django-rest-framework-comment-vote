from rest_framework import serializers
from .models import vote

class vote_serializer(serializers.ModelSerializer):
    class Meta:
        model = vote
        fields = [
            "user_id",
            "pd_id",
        ]