from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView

from user.models import User  # DocumentName


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
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'social_security_number']

    def get_object(self, queryset=None):
        return self.request.user


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user:list')
