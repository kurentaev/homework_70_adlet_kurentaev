from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Tasks
from webapp.forms import TasksListForm
from webapp.models import Projects


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class TaskAddView(PermissionRequiredMixin, SuccessDetailUrlMixin, CreateView):
    template_name = 'task/task_create.html'
    form_class = TasksListForm
    model = Tasks
    permission_required = 'webapp.add_tasks'

    def has_permission(self):
        return super().has_permission() or self.request.user.is_superuser


class TaskUpdateView(PermissionRequiredMixin, SuccessDetailUrlMixin, UpdateView):
    template_name = 'task/task_update.html'
    form_class = TasksListForm
    model = Tasks
    context_object_name = 'task'
    permission_required = 'webapp.change_tasks'

    def has_permission(self):
        return (super().has_permission() and self.request.user in self.get_object().project.user.all() or
                self.request.user.is_superuser)


class TaskView(DetailView):
    template_name = 'task/task.html'
    model = Tasks
    context_object_name = 'task'


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'task/task_delete.html'
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_tasks'

    def has_permission(self):
        return (super().has_permission() and self.request.user in self.get_object().project.user.all() or
                self.request.user.is_superuser)
