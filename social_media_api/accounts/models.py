from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Why this exists:
    - Allows adding social-media-specific fields
    - Prevents painful migrations later
    """

    # Short biography for user profiles
    bio = models.TextField(blank=True)

    # Optional profile picture
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    # Self-referential many-to-many relationship for followers
    # symmetrical=False allows one-way following (A follows B ≠ B follows A)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
