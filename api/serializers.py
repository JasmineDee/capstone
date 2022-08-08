from operator import truediv
from rest_framework import serializers
from django.contrib.auth import get_user_model
from journal.models import Entry

from main.models import Task

class NestedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'created')


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class TaskSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(read_only=True, source='user')
    class Meta:
        model = Task
        fields = ('id','user','user_detail', 'title', 'created')

class UserSerializer(serializers.ModelSerializer):
    tasks_detail = NestedTaskSerializer(many=True, source='tasks', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'tasks', 'tasks_detail')        

class EntrySerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(read_only=True, source='user')
    class Meta:
        model = Entry
        fields = ('id','user','user_detail', 'text', 'date_posted')

class NestedEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = ('id', 'text', 'date_posted')
