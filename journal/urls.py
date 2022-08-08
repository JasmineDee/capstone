from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='entries'),
    path('add/', views.add, name='add')
]