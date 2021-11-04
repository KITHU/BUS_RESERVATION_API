from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, max_length=16, write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','role','password']

    def validate(self, attr):
        username = attr.get('username', '')
        email = attr.get('email', '')
        if not username.isalnum():
            raise serializers.ValidationError('password should only contain alphanumeric')
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=16, min_length=4, required=True, write_only=True)
    username = serializers.CharField(read_only=True)
    tokens = serializers.CharField(read_only=True)
    class Meta:
        model = User 
        fields = ['id','email', 'password','username','tokens']

    def validate(self, attr):
        email = attr.get('email', '')
        password = attr.get('password', '')
      
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return {
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'role' : user.role,
            'tokens': user.tokens
        }
