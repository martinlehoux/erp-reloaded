from django.views.generic import ListView, DetailView

from user.models import User


class UserList(ListView):
    queryset = User.objects.all()
    context_object_name = 'user_set'


class UserDetail(DetailView):
    model = User
    context_object_name = 'user'
