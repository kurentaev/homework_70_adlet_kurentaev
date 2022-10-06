from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from webapp.models import Tasks
from webapp.forms import TasksListForm


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context


class TaskAddView(TemplateView):
    template_name = 'task_create.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TasksListForm()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = TasksListForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('todo_detail', pk=task.pk)
        return render(request, self.template_name, context={'form': form})


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TasksListForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs['pk'])
        form = TasksListForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('todo_detail', pk=task.pk)
        return render(request, self.template_name, context={'form': form})

#
#
# def delete_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'article_confirm_delete.html', context={'article': article})
#
#
# def confirm_delete(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     article.delete()
#     return redirect('index')
