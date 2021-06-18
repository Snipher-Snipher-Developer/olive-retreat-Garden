from rest_framework import serializers

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "username",
            "first_name",
            "second_name",
            "phone",
            "email",
            "decoration",
            "date_booked"
        )
