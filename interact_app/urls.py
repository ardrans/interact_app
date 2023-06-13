# from django.urls import path
# from . import views
from django.urls import re_path
from django.urls import path, include
from .views import LoginView
from rest_framework.routers import DefaultRouter
from .views import (
    UsersListApiView,
    UsersDetailApiView,
    PostViewSet,
)

# router = DefaultRouter()
# router.register(r'posts', PostViewSet, basename='post')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user_register/', UsersListApiView.as_view()),
    path('verify_email/<str:key>/', UsersListApiView.as_view()),
    path('del/<int:user_id>/', UsersListApiView.as_view(), name='delete'),
    path('create_post/', PostViewSet.as_view(), name='post'),
    #path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    #path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'delete': 'delete'}), name='post-detail'),
]

#'put': 'update', 'patch': 'partial_update'


# urlpatterns = [
#     #path('', views.tasks_list, name='tasks_list'),
#     path('user_register/', views.create_user, name='create_user'),
#     path('verify_email/<str:key>/', views.verify_email, name='verify_email'),
#
#
# ]