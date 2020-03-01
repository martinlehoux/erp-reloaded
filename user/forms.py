from django import forms

from user.models import Document, User


class UploadDocumentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Document
        fields = ['name', 'file', 'user']
