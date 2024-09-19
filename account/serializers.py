from rest_framework import serializers
from .models import Institute
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class InstituteRegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length=68, min_length=6, write_only= True)
    password2=serializers.CharField(max_length=68, min_length=6, write_only= True)

    class Meta:
        model=Institute
        fields=['email','name','password','password2']

    def validate(self, attrs):
        password=attrs.get('password','')
        password2=attrs.get('password2','')
        if password != password2:
            raise serializers.ValidationError("Passwords did not match")
        return attrs   
    
    def create(self, validated_data):
        institute=Institute.objects.create_institute(
        email=validated_data['email'],
        name=validated_data.get('name'),
        password=validated_data.get('password')
        )
        return institute