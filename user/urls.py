from django.urls import path
from django.views.generic import RedirectView

from user.views import (ListActiveUser, ListArchiveUser, MeUser, ShowUser,
                        upload_document)

app_name = 'user'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='user:list-active', permanent=True)),
    path('list/', ListActiveUser.as_view(), name='list-active'),
    path('list/archive', ListArchiveUser.as_view(), name='list-archive'),
    path('me/', MeUser.as_view(), name='me'),
    path('me/upload', upload_document, name='upload'),
    path('show/<int:pk>', ShowUser.as_view(), name='show'),
]
