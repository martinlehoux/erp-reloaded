import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UploadTo:
    def __init__(self, fieldname):
        self.fieldname = fieldname

    def __call__(self, user, filename):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        return f'user/{user.username}/{self.fieldname}{ext}'

    def deconstruct(self):
        return ('user.models.UploadTo', [self.fieldname], {})


class User(AbstractUser):
    photo = models.ImageField(
        upload_to=UploadTo('photo'),
        null=True,
        blank=True,
    )
    social_security_number = models.CharField(
        max_length=64,
        blank=True,
    )
    phone_number = PhoneNumberField(
        blank=True,
        null=True
    )


class DocumentName(models.Model):
    name = models.CharField(
        max_length=64
    )

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.ForeignKey(
        to='user.DocumentName',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE
    )
