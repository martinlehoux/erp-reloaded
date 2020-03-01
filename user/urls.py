from django.urls import path

from user.views import UserDetail, UserList

app_name = 'user'
urlpatterns = [
    path('list/', UserList.as_view(), name='list'),
    path('show/<int:pk>', UserDetail.as_view(), name='show')
]
