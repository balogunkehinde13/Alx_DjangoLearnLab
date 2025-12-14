from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

"""
Serializers convert:
- Incoming JSON → Python objects (validation)
- Python objects → JSON (response data)

They are NOT controllers — just translators.
"""


class RegisterSerializer(serializers.ModelSerializer):
    """
    Handles user registration.
    Creates a user and immediately generates an auth token.
    """

    # Password should never be returned in responses
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio']

    def create(self, validated_data):
        """
        Create a new user using Django's built-in user manager.
        """

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )

        # Create a token for API authentication
        Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    """
    Validates login credentials.
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Authenticate the user using Django's auth system.
        """

        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing and updating user profiles.
    """

    # Computed fields (not stored in the database)
    followers_count = serializers.IntegerField(
        source='followers.count',
        read_only=True
    )
    following_count = serializers.IntegerField(
        source='following.count',
        read_only=True
    )

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'bio',
            'profile_picture',
            'followers_count',
            'following_count'
        ]
