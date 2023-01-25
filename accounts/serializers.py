
from datetime import datetime, timedelta
from rest_framework import serializers
from accounts.models import UserAccount

class AppUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(max_length = 15)
    class Meta:
        model = UserAccount
        exclude = ('is_staff', 'user_permissions', 'groups',  'is_superuser')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_type = validated_data.get("user_type")
        if user_type == "seller":
            validated_data['is_admin'] = True
        elif user_type == "buyer":
            validated_data['is_admin'] = False
        else:
            return serializers.ValidationError("Please select one option")

        validated_data['is_active'] = True
        del validated_data['user_type']
       
        user = UserAccount.objects.create_user(**validated_data)
        return user

    def validate_email(self, value):
        if UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already taken')
        return value