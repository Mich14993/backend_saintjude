
from django.urls import path

from api_v1.user.views import PermissionListCreate, PermissionRetrieveUpdateDestroy


urlpatterns=[
    path('permissions/',PermissionListCreate.as_view(),name='permission-list-create'),
    path('permissions/<int:pk>/',PermissionRetrieveUpdateDestroy.as_view(), name='permission-detail')
]