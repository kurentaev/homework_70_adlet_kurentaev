from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects, Tasks
from webapp.forms import ProjectForm, ProjectTasksForm, ProjectUserAddForm


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


class CustomUserPassesTestMixin(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProjectAddView(CustomUserPassesTestMixin, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Projects
    groups = ['manager']


class ProjectUpdateView(CustomUserPassesTestMixin, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    model = Projects
    context_object_name = 'project'
    groups = ['manager']


class ProjectTaskAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'project/project_task_create.html'
    form_class = ProjectTasksForm
    model = Tasks
    permission_required = 'webapp.add_task'

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)

    def has_permission(self):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.user.all()


class ProjectDeleteView(CustomUserPassesTestMixin, LoginRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Projects
    context_object_name = 'project'
    success_url = reverse_lazy('projects')
    groups = ['manager']


class ProjectUserAddView(CustomUserPassesTestMixin, PermissionRequiredMixin, UpdateView):
    model = Projects
    template_name = 'project/project_add_user.html'
    form_class = ProjectUserAddForm
    permission_required = 'webapp.add_task'
    groups = ['manager', 'lead']

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)

    def has_permission(self):
        return Projects.objects.filter(user=self.request.user, pk=self.get_object().pk) and super().has_permission()
