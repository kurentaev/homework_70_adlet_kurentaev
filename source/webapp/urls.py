from django.urls import path
from webapp.views.base import IndexView
from webapp.views.tasks import TaskView, TaskAddView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo_list/', IndexView.as_view(), name='home'),
    path('todo_list/<int:pk>', TaskView.as_view(), name='todo_detail'),
    path('todo_list/add/', TaskAddView.as_view(), name='todo_add'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='todo_delete'),
    path('todo_list/update/<int:pk>', TaskUpdateView.as_view(), name='todo_update'),
]
