from user.views import UserList, UserDetail
from django.urls import path

app_name = 'user'
urlpatterns = [
    path('list/', UserList.as_view(), name='list'),
    path('show/<int:pk>', UserDetail.as_view(), name='show')
]
