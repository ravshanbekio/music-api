from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    """ Custom user's manager """

    def create_user(self, username, phone_number,password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have an username!")
        if not phone_number:
            raise ValueError("Users must have an phone number!")
        
        user = self.model(
                phone_number=phone_number,
                username=username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, phone_number, password):
        user = self.create_user(
            username=username,
            phone_number=phone_number,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user """

    full_name = models.CharField(max_length=102)
    username = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField(help_text="Enter your phone number")
    email = models.EmailField(blank=True, null=True)
    profile_photo = models.FileField()
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number',]

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label ):
        return True
