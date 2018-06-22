from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class BerryManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self):
        pass


class Berry(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    nickname = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BerryManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    @property
    def is_staff(self):
        return False
