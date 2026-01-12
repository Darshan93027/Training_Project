from django.db import models
from django.contrib.auth.models import AbstractUser


class cuser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return f"Email is {self.email}"



