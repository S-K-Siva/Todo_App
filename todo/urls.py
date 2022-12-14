from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('',views.TaskList.as_view(), name = "Task"),
    path('todolist/<int:pk>',views.TaskDetail.as_view(), name = "TaskDetail"),
    path('todolist/create',views.CreateTask.as_view(),name = "TaskCreate"),
    path('login/',views.LoginPage.as_view(),name = "login"),
    path('register/',views.RegisterView.as_view(),name = "register"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('todolist-update/<int:pk>',views.UpdateTask.as_view(),name = "Task-Update"),
    path('todolist-delete/<int:pk>',views.DeleteTask.as_view(),name="TaskDelete"),
]