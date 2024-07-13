
from django.urls import path

from api_v1.user.views import UserDetailUpdateDestroy, UserListCreate


urlpatterns = [
    path('users/',UserListCreate.as_view(),name='user-list-create'),
    path('users/<int:pk>/',UserDetailUpdateDestroy.as_view(),name='user-detail')    
]
