from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_user_name(self):
        """Retrieve full name of the  user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name

    def __str__(self):
        """Return strign representation of the user"""
        return self.email


status = (('unassigned', 'UNASSIGNED'), ('assigned', 'ASSIGNED'), ('completed', 'COMPLETED'))

duration = (('1 hr', '1'), ('2 hr', '2'), ('3 hr', '3'), ('4 hr', '4'), ('5 hr', '5'))


class TaskDetails(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(max_length=500)
    assigned_to = models.CharField(max_length=100,blank=True)
    created_by = models.CharField(max_length=100)
    task_duration = models.CharField(max_length=10, choices=duration, default='1 hr')
    task_status = models.CharField(max_length=10, choices=status, default='unassigned')

    def __str__(self):
        """return task details"""
        return f'{self.task_id} == {self.task_name}'

