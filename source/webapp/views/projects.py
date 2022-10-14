from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects, Tasks
from webapp.forms import ProjectForm, ProjectTasksForm


class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.filter(is_deleted=False)
        return context


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectAddView(SuccessDetailUrlMixin, CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Projects


class ProjectUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    model = Projects
    context_object_name = 'project'


class ProjectTaskAddView(CreateView):
    template_name = 'project/project_task_create.html'
    form_class = ProjectTasksForm
    model = Tasks

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    model = Projects
    context_object_name = 'project'
    success_url = reverse_lazy('projects')
