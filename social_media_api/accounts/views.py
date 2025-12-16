from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType

from notifications.models import Notification

from .models import User as CustomUser
from .serializers import UserProfileSerializer

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer
)


User = get_user_model()


"""
Views handle:
- HTTP requests
- Calling serializers
- Returning HTTP responses
- follow / unfollow functionality
"""


class RegisterView(APIView):
    """
    Registers a new user and returns an authentication token.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)

            return Response(
                {
                    'token': token.key,
                    'user': UserProfileSerializer(user).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Authenticates a user and returns an existing token.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'user': UserProfileSerializer(user).data
            }
        )


class ProfileView(APIView):
    """
    Retrieve or update the authenticated user's profile.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    """
    Allow an authenticated user to follow another user.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        target_user = get_object_or_404(self.queryset, id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Follow the user
        request.user.following.add(target_user)

        # 🔔 CREATE NOTIFICATION HERE
        Notification.objects.create(
            recipient=target_user,
            actor=request.user,
            verb='started following you',
            content_type=ContentType.objects.get_for_model(target_user),
            object_id=target_user.id
        )

        return Response(
            {"detail": f"You are now following {target_user.username}."},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    """
    Allow an authenticated user to unfollow another user.
    """

    permission_classes = [permissions.IsAuthenticated]

    # 👇 REQUIRED by spec
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        target_user = get_object_or_404(self.queryset, id=user_id)

        request.user.following.remove(target_user)

        return Response(
            {"detail": f"You unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
