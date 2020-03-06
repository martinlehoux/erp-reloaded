from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, UpdateView
from django_filters import FilterSet, views

from customer.forms import ContactForm, ExchangeForm
from customer.models import ActivityArea, BusinessSize, Country, Customer
from erp_reloaded.forms import (CountrySelectField, InputField, SearchForm,
                                SelectField)
from user.models import User


class FilterCustomer(FilterSet):
    class Meta:
        model = Customer
        fields = ['name', 'size', 'country']


class ListCustomer(views.FilterView):
    queryset = Customer.objects.all()
    context_object_name = 'customer_set'
    template_name = 'customer/list.html'
    filterset_class = FilterCustomer
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm([
            InputField('name'),
            SelectField('size', options=BusinessSize.objects.all()),
            CountrySelectField("country", options=Country.objects.all(), clearable=True),
        ])
        return context


class CreateCustomer(CreateView):
    model = Customer
    template_name = 'customer/create.html'
    fields = ['name', 'website', 'activity_area_set', 'size', 'address', 'zip_code', 'city', 'country']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity_area_set'] = ActivityArea.objects.all()
        context['business_size_set'] = BusinessSize.objects.all()
        context['country_set'] = Country.objects.all()
        return context


class ShowCustomer(UpdateView):
    model = Customer
    template_name = 'customer/show.html'
    context_object_name = 'customer'
    fields = ['name', 'website', 'activity_area_set', 'size', 'address', 'zip_code', 'city', 'country']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity_area_set'] = ActivityArea.objects.all()
        context['business_size_set'] = BusinessSize.objects.all()
        context['country_set'] = Country.objects.all()
        context['contact_set'] = self.object.contact_set.prefetch_related('exchange_set', 'exchange_set__user').all()
        context['user_set'] = User.objects.filter(is_active=True)
        return context


@require_http_methods(["POST"])
def create_contact(request, customer_pk):
    data = request.POST.copy()
    data['customer'] = customer_pk
    form = ContactForm(data)
    if not form.is_valid():
        for field, message in form.errors.items():
            messages.error(request, f"Failed to upload {field}: {message}")
        return redirect(reverse_lazy('customer:show', kwargs={'pk': customer_pk}))
    contact = form.save()
    messages.success(request, f"Contact {contact} created")
    return redirect(reverse_lazy('customer:show', kwargs={'pk': customer_pk}))


@require_http_methods(["POST"])
def create_exchange(request, customer_pk):
    data = request.POST.copy()
    data['customer'] = customer_pk
    form = ExchangeForm(data)
    if not form.is_valid():
        for field, message in form.errors.items():
            messages.error(request, f"Failed to create exchange {field}: {message}")
        return redirect(reverse_lazy('customer:show', kwargs={'pk': customer_pk}))
    exchange = form.save()
    messages.success(request, f"Exchange {exchange} created for customer")
    return redirect(reverse_lazy('customer:show', kwargs={'pk': customer_pk}))
