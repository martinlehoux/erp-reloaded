from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from django_filters import views, FilterSet

from erp_reloaded.forms import InputField, SelectField, CountrySelectField, SubmitField, SearchForm
from user.forms import UploadDocumentForm
from user.models import Document, DocumentName, User


class FilterUser(FilterSet):
    class Meta:
        model = User
        fields = ['username']


class ListActiveUser(ListView):
    queryset = User.objects.filter(is_active=True)
    context_object_name = 'user_set'
    template_name = 'user/list-active.html'
    ordering = ['username']


class ListArchiveUser(views.FilterView):
    queryset = User.objects.filter(is_active=False)
    paginate_by = 25
    context_object_name = 'user_set'
    template_name = 'user/list-archive.html'
    filterset_class = FilterUser
    ordering = ['-date_left']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm([
            InputField('name'),
        ])
        return context
    

class ShowUser(UpdateView):
    model = User
    template_name = 'user/show.html'
    context_object_name = 'user'
    fields = ['is_active', 'groups', 'date_left']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class MeUser(UpdateView):
    template_name = 'user/me.html'
    context_object_name = 'user'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'social_security_number', 'biography', 'photo']

    def get_success_url(self):
        return reverse('user:me')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document_name_set'] = DocumentName.objects.all()
        return context


# TODO: Protected and served by nginx
def upload_document(request):
    if request.method != 'POST':
        return redirect(reverse('user:me'))
    form = UploadDocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        for field, message in form.errors.items():
            messages.error(request, f"Failed to upload {field}: {message}")
        return redirect(reverse('user:me'))
    form.instance.user = request.user
    old_doc = Document.objects.filter(user=request.user, name=form.instance.name).first()
    if old_doc:
        old_doc.delete()
    document = form.save()
    messages.success(request, f"Uploaded {document.name}")
    return redirect(reverse('user:me'))
