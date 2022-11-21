from django.urls import path
from api.views import TasksView, ProjectsView

urlpatterns = [
    path('tasks/<int:pk>/', TasksView.as_view(), name='tasks'),
    path('projects/<int:pk>/', ProjectsView.as_view(), name='projects'),
]
