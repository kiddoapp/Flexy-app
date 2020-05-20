from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
# from django.utils.trasaction import ugettext_lazy as _



# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    # email = models.EmailField(_('email address'),unique=True)
    Age = models.PositiveIntegerField(unique=False)
    phone_number = models.PositiveIntegerField(unique=True)
    staysignin = models.BooleanField(blank=False, unique=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','fist_name','last_name', 'Age', 'phone_number', 'staysignin' ]

    def __str__(self):
        return "{}".format(self.email)
