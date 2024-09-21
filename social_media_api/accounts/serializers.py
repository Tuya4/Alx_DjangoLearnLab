from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Handle password properly using set_password
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            bio=validated_data.get('bio'),
            profile_picture=validated_data.get('profile_picture'),
        )
        user.set_password(validated_data['password'])  # Set password correctly
        user.save()
        return user    