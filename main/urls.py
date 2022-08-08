from django.urls import path
from . import views
from .views import TaskDelete
from journal.views import add, index


urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/',views.logOut, name="logout"),
    path('timer/',views.timer, name= 'timer'),
    path('', views.TaskList.as_view(), name ='tasks'),
    path('<int:pk>/', views.TaskDetail.as_view(), name ='task'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name ='delete'),
    
]

