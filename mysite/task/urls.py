from django.urls import path
from .views import TodoListViewSet


urlpatterns = [
    path('', TodoListViewSet.as_view({'get': 'list', 'post': 'create'}), name= 'todo_list'),
    path('<int:pk>/', TodoListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='todo_detail'),
]
