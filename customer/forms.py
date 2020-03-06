from django import forms

from customer.models import Contact, Exchange


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = '__all__'
