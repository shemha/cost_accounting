# venv/lib/python3.8/site-packages/django/db/modelsディレクトリ
from django.db import models
# venv/lib/python3.8/site-packages/django/contrib/auth/models.pyの'PermissionsMixin'クラス
from django.contrib.auth.models import PermissionsMixin
# venv/lib/python3.8/site-packages/django/contrib/auth/base_user.pyの'AbstractBaseUser'クラス
from django.contrib.auth.base_user import AbstractBaseUser
# venv/lib/python3.8/site-packages/django/utils/timezone.pyファイル
from django.utils import timezone
# venv/lib/python3.8/site-packages/django/contrib/auth/base_user.pyの'BaseUserManager'クラス
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    """カスタムユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    email = models.EmailField("メールアドレス", unique=True)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"