from django.urls import path
from django.views.generic import RedirectView

from customer.views import ListCustomer, CreateCustomer, ShowCustomer, create_contact


app_name = 'customer'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='customer:list', permanent=True)),
    path('list/', ListCustomer.as_view(), name='list'),
    path('create/', CreateCustomer.as_view(), name='create'),
    path('show/<int:pk>', ShowCustomer.as_view(), name='show'),
    path('show/<int:customer_pk>/create-contact', create_contact, name='create-contact')
]
