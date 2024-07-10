from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

USER_TYPE_CHOICES = (
    ('adminuser', 'AdminUser'),
    ('Donor', 'Donor'),
)

class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Add related_name for groups
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='user'
    )

    # Add related_name for user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='user'
    )
