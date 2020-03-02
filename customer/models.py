import os

from django.db import models
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField


def upload_logo_to(customer, filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f'customer/{customer.id}/logo{ext}'


class Customer(models.Model):
    name = models.CharField(max_length=256, unique=True)
    logo = models.ImageField(upload_to=upload_logo_to, null=True, blank=True)
    website = models.URLField(blank=True)
    activity_area_set = models.ManyToManyField(to='customer.ActivityArea')
    size = models.ForeignKey(to='customer.BusinessSize', on_delete=models.PROTECT)
    address = models.CharField(max_length=256, blank=True)
    zip_code = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    country = models.ForeignKey(to='customer.Country', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer:show", kwargs={"pk": self.pk})

    @property
    def issues(self):
        problems = []
        if self.contact_set.count() == 0:
            problems.append("Customer has no contact")
        if not self.address or not self.zip_code or not self.city:
            problems.append("Customer address incomplete")
        return problems


class Country(models.Model):
    name = models.CharField(max_length=256, unique=True)
    # https://fomantic-ui.com/elements/flag.html
    icon = models.CharField(max_length=8, blank=True)
    value_added_tax = models.DecimalField(decimal_places=4, max_digits=5, default='0.2000')

    def __str__(self):
        return self.name


class ActivityArea(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class BusinessSize(models.Model):
    name = models.CharField(max_length=256, unique=True)
    short = models.CharField(max_length=32, unique=True, blank=True)

    def __str__(self):
        return f"{self.short} - {self.name}"


class Contact(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    office = models.CharField(max_length=256, blank=True)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    customer = models.ForeignKey(to='customer.Customer', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.customer})"
