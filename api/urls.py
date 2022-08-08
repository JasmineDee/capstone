from django.urls import URLPattern, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')
router.register('users', views.UserViewSet, basename='users')
router.register('entries', views.EntryViewSet, basename='entries')


urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserView.as_view())
]

#urlpatterns = [
 #   path('', views.TaskApiView.as_view()),
#]