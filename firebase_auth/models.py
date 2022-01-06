import uuid as uuid_lib

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4)

    def __str__(self):
        return self.user.username