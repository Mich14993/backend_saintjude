
from django.urls import path

from api_v1.user.views import UserListCreate, UserRetrieveUpdateDestroy


urlpatterns = [
    path('users/',UserListCreate.as_view(),name='user-list-create'),
    path('users/<int:pk>/',UserRetrieveUpdateDestroy.as_view(),name='user-detail')    
]
