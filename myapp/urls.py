from django.urls import path
from . import views
urlpatterns = [
    path('', views.TodoList, name="TodoList"),
    path('detail/<uuid:pk>/' , views.TodoDetail, name="TodoDetail"),
    path('update/<uuid:pk>/' , views.TodoUpdate, name="TodoUpdate"),
    path('delete/<uuid:pk>/' , views.TodoDelete, name="TodoDelete"),
]