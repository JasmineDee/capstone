from django.urls import path
from . import views


urlpatterns = [

    path('', views.TaskList.as_view(), name ='tasks'),
    path('<str:pk>/', views.TaskDetail.as_view(), name ='task'),
    path('<str:pk>/task_delete', views.TaskDelete.as_view(), name ='delete'),

]

