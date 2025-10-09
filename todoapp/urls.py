from django.urls import path
from . import views

urlpatterns = [
    path('api/task_list', views.task_list, name='index'),
]