

from rest_framework import viewsets, permissions
from .models import TodoList
from .serializer import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

