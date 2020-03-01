from django.urls import path
from django.views.generic import RedirectView

from user.views import UserDelete, UserList, UserMe, UserShow, upload_document

app_name = 'user'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='user:list', permanent=True)),
    path('list/', UserList.as_view(), name='list'),
    path('me/', UserMe.as_view(), name='me'),
    path('me/upload', upload_document, name='upload'),
    path('show/<int:pk>', UserShow.as_view(), name='show'),
    path('delete/<int:pk>', UserDelete.as_view(), name='delete'),
]
