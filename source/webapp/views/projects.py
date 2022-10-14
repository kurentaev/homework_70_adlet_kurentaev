from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects, Tasks
from webapp.forms import ProjectForm, ProjectTasksForm
from webapp.forms import TasksSearchForm


class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    model = Projects
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return TasksSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        # queryset = super(IndexView, self).get_queryset().exclude(is_deleted=True)
        queryset = super(ProjectIndexView, self).get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


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
    success_url = reverse_lazy('projects')
