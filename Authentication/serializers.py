from rest_framework import serializers
from .models import cuser
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=8, min_length=6, write_only=True)
    class Meta:
        model = cuser
        fields = ['email', 'username', 'password']
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs
    def create(self, validated_data):
        return cuser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6,write_only=True)
    username = serializers.CharField(max_length=255, min_length=3)
   

    class Meta:
        model = cuser
        fields = ['password','username']
    def validate(self, attrs):
        username = attrs.get('username','')
        password = attrs.get('password','')
        user = authenticate(username=username, password=password)
                
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        
        # Generate JWT tokens using SimpleJWT
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        return {
            'email': user.email,
            'username': user.username,
            'access': str(access_token),
            'refresh': str(refresh)
        }

    
   