from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.TodoList, name="TodoList"),
    path('toggle-completed/<uuid:todo_id>/', views.toggle_completed, name="toggle_completed"),
]