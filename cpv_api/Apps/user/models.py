from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """
        Manager for UserProfile
    """

    def create_user(self, email, password=None, **extra_fields):
    #def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """ Create a new UserProfile """
        if not email:
            raise ValueError('User must have an email!')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        #user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)

        user.set_password(password)
        #user.save(using=self._db)
        user.save()

        return user


    def create_superuser(self, email, **extra_fields):
    #def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        user = self.create_user(email, **extra_fields)
        #user = self.create_user(email, first_name, last_name, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True

        user.save()
        #user.save(using=self._db)

        return user


def user_photo_directory_path(instance, filename):
    """ 
        Profile Photo will be uploaded
        to MEDIA_ROOT/profile/email/<filename>
    """
    return f'profile/{instance.email}/{filename}'


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        User Model for the system
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    employee_number = models.PositiveSmallIntegerField(
        unique=True,
        blank=True,
        null=True,
    )
    department = models.ForeignKey('Department',
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True)
    photo = models.ImageField(upload_to=user_photo_directory_path,
                              blank=True,
                              default='static/default-profile-photo.png')
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)



    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def get_full_name(self):
        """ Get user full name """
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{}'.format(self.email)

    def _in_group(self, group):
        return self.groups.filter(name=group).exists()

    @property
    def is_admin(self):
        return self._in_group('admin')
    
    @property
    def is_gps(self):
        return self._in_group('gps')

    @property
    def is_regular(self):
        return self._in_group('regular')


class Department(models.Model):
    """
        Department where user is located 
    """
    name = models.CharField(max_length=255,
                            unique=True,
                            null=True)
    
    def short_name(self):
        """ Get Department short name (acronym) """
        list_words = str(self.name).split()
        final_acro = ""
        for i in list_words:
            final_acro+=i[0].upper()
            #final_acro+=i[1:3]
        return final_acro

    def __str__(self):
        return '{}'.format(self.name)
