from rest_framework import serializers
from .models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Farmer
        fields = ['email', 'full_name', 'phone_number', 'age', 'gender', 'farm_name', 'address', 'city', 'state', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        farmer = Farmer(**validated_data)
        farmer.set_password(password)
        farmer.save()
        return farmer
