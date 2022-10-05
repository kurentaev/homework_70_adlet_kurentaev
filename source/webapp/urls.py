from django.urls import path

from webapp.views.base import IndexView
# from webapp.views.tasks import add_view
# from webapp.views.tasks import task_view
# from webapp.views.tasks import delete_view
# from webapp.views.tasks import confirm_delete
# from webapp.views.tasks import update_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('todo_list/add/', add_view, name='todo_add'),
    # path('todo_list/', index_view, name='home'),
    # path('todo_list/<int:pk>', task_view, name='todo_detail'),
    # path('delete_task/<int:pk>', delete_view, name='delete'),
    # path('todo_list/confirm_delete/<int:pk>', confirm_delete, name='confirm_delete'),
    # path('todo_list/update/<int:pk>', update_view, name='todo_update'),
]
