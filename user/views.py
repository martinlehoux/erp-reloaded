from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView

from user.forms import UploadDocumentForm
from user.models import Document, DocumentName, User


class UserList(ListView):
    queryset = User.objects.all()
    context_object_name = 'user_set'


class UserShow(UpdateView):
    model = User
    template_name = 'user/user_show.html'
    context_object_name = 'user'
    fields = ['is_active', 'groups', 'date_left']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class UserMe(UpdateView):
    template_name = 'user/user_me.html'
    context_object_name = 'user'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'social_security_number', 'biography']

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


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user:list')
