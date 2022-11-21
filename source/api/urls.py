from django.urls import path
from api.views import TasksView

urlpatterns = [
    path('tasks/<int:pk>/', TasksView.as_view(), name='tasks'),
]
