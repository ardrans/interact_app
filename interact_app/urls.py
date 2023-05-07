from django.urls import path
from . import views

urlpatterns = [
    #path('', views.tasks_list, name='tasks_list'),
    path('user_register/', views.create_user, name='create_user'),


]