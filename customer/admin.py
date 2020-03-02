from django.contrib import admin

from customer.models import (ActivityArea, BusinessSize, Contact, Country,
                             Customer)

admin.site.register(Customer)
admin.site.register(Country)
admin.site.register(ActivityArea)
admin.site.register(BusinessSize)
admin.site.register(Contact)
