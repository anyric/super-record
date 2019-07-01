from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
)

class UserManager(BaseUserManager):
    """Class to manage the creation of user objects"""

    def create_user(self, username, email, password=None):
        """Creates and returns a user object
        Arguments:
        username: the string to use as username
        email: the string to use as email
        password: the string to use as password

        Optionals:
        is_staff: Boolean to indicate a user is staff or not
        is_admin: Boolean to indicate a user is an admin or not
        is_active: Boolean to indicate a user can login or not

        Return:
            A user object
        """
        if not username:
            raise ValueError('Users must have a username')
        
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(username=username,email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, email, password):
        """Creates a staff user object
        Arguments:
        username: the string to use as username
        email: the string to use as email
        password: the string to use as password

        Return:
            A user object
        """
        user_obj = self.create_user(username, email, password)
        user_obj.is_staff=True
        user_obj.is_active=True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, email, password):
        """Creates an admin user object
        Arguments:
        username: the string to use as username
        email: the string to use as email
        password: the string to use as password

        Return:
            A user object
        """
        user_obj = self.create_user(username, email, password)
        user_obj.is_staff=True
        user_obj.is_admin=True
        user_obj.is_active=True
        return user_obj


class User(AbstractBaseUser):
    """
    Class for creating user implementing the abstract 
    base user and the permission class 
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        """Returns a string representation of this `User`."""
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
