from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#UserProfile
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name','username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','username', 'email', 'password')
        extra_kwargs = {
            'id':{'read_only':True},
            'password':{'write_only':True},
            'email':{'required':False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name= validated_data['last_name'],
            username=validated_data['username'], 
            email=validated_data['email'],
            password=validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
