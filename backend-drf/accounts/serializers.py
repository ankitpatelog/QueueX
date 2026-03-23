from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.base_user import BaseUserManager
import random

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        email = validated_data['email']
        email = BaseUserManager.normalize_email(email)

        # check email exists
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})

        # generate username
        randint = random.randint(1000, 9999)
        username = email.split('@')[0] + str(randint)

        user = User.objects.create_user(
            email=email,
            username=username,
            password=validated_data['password'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )

        return user