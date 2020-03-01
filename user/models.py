import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
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


def upload_document_to(document, filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f'user/{document.user.username}/{document.name}{ext}'


class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo('photo'), null=True, blank=True)
    social_security_number = models.CharField(max_length=64, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    date_left = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('user:show', kwargs={'pk': self.pk})


class DocumentName(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=32, default="file")

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.ForeignKey(to='user.DocumentName', on_delete=models.PROTECT)
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_document_to)

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return f"{self.user} - {self.name}"
