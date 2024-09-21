from rest_framework import serializers
from rest_framework.authtoken.models import Token  
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField()
    bio = serializers.CharField(allow_blank=True, required=False)
    profile_picture = serializers.ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']

    def create(self, validated_data):
        # Use get_user_model to ensure compatibility with custom user models
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            bio=validated_data.get('bio'),
            profile_picture=validated_data.get('profile_picture'),
        )
        # Set the password properly using set_password method
        user.set_password(validated_data['password'])
        user.save()
        
        # Create a token for the user upon successful registration
        Token.objects.create(user=user)
        return user
