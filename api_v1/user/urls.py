
from django.urls import path

from api_v1.user.views import GroupDetailUpdateDestroy, GroupListCreate, PermissionDetailUpdateDestroy, PermissionListCreate, UserDetailUpdateDestroy, UserListCreate


urlpatterns = [
    path('users/',UserListCreate.as_view(),name='user-list-create'),
    path('users/<int:pk>/',UserDetailUpdateDestroy.as_view(),name='user-detail'),
    path('permissions/',PermissionListCreate.as_view(),name='user-list-create'),
    path('permissions/<int:pk>',PermissionDetailUpdateDestroy.as_view(),name='user_detail'),
    path('groups/',GroupListCreate.as_view(),name='group-list-create'),
    path('groups/<int:pk>',GroupDetailUpdateDestroy.as_view(),name='group-detail')    
]
