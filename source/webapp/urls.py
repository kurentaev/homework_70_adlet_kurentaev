from django.urls import path

from webapp.views.base import IndexView
from webapp.views.tasks import TaskView
from webapp.views.tasks import TaskAddView
# from webapp.views.tasks import delete_view
# from webapp.views.tasks import confirm_delete
from webapp.views.tasks import TaskUpdateView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo_list/', IndexView.as_view(), name='home'),
    path('todo_list/<int:pk>', TaskView.as_view(), name='todo_detail'),
    path('todo_list/add/', TaskAddView.as_view(), name='todo_add'),
    # path('delete_task/<int:pk>', delete_view, name='delete'),
    # path('todo_list/confirm_delete/<int:pk>', confirm_delete, name='confirm_delete'),
    path('todo_list/update/<int:pk>', TaskUpdateView.as_view(), name='todo_update'),
]
