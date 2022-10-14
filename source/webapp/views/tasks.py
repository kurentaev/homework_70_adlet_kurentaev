from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Tasks
from webapp.forms import TasksListForm


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class TaskAddView(SuccessDetailUrlMixin, CreateView):
    template_name = 'task/task_create.html'
    form_class = TasksListForm
    model = Tasks


class TaskUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'task/task_update.html'
    form_class = TasksListForm
    model = Tasks
    context_object_name = 'task'


class TaskView(DetailView):
    template_name = 'task/task.html'
    model = Tasks
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    template_name = 'task/task_delete.html'
    model = Tasks
    success_url = reverse_lazy('index')
