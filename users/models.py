from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from ledger.models import IncomesCategory, ExpensesCategory


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    telegram_id = models.BigIntegerField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    currency = models.CharField(max_length=10, default='USD')
    key = models.CharField(max_length=15, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def get_incomes_category(self):
        return (self.incomes_category.all())

    def get_expenses_category(self):
        return (self.expenses_category.all())
