from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.tag


class BookMark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='bookmarks')
    category = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class AuthUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address!")
        if not username:
            raise ValueError("Users must have a username!")

        user = self.model(username=username, email=self.normalize_email(email),)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MarkUser(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(r'[0-9a-zA-Z]*$', message='Please only use alphanumeric characters.')

    username = models.CharField(unique=True, max_length=20, validators=[alphanumeric])
    email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    # Custom Fields
    bookmarks = models.ManyToManyField(BookMark, related_name='bookmarks')

    objects = AuthUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        fullname = self.first_name + " " + self.last_name
        return fullname

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email


