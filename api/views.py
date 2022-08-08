from django import views
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model

from main.models import Task
from journal.models import Entry
from .serializers import TaskSerializer, UserSerializer, EntrySerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthorOrReadOnly]



#class TaskApiView(generics.ListCreateAPIView):

    
