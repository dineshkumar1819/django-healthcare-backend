from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctor

# Serializer to handle user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Model we are serializing (User)
        fields = ['username', 'email', 'password']  # Fields to include in the serializer
        extra_kwargs = {'password': {'write_only': True}}  # Password is write-only for security

    # Overriding the create method to ensure password is hashed properly during user creation
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  # Creates a new user with hashed password


# Serializer to handle Patient data (CRUD operations)
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient  # Model we are serializing (Patient)
        fields = '__all__'  # Include all fields in the model


# Serializer to handle Doctor data (CRUD operations)
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor  # Model we are serializing (Doctor)
        fields = '__all__'  # Include all fields in the model


# Serializer to handle Patient-Doctor relationship (Mapping)
class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctor  # Model we are serializing (PatientDoctor mapping)
        fields = '__all__'  # Include all fields in the model
