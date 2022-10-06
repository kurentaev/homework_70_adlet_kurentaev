from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from webapp.models import Tasks
# from webapp.forms import ArticleForm
# from webapp.models.articles import StatusChoices


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context


# def add_view(request):
#     form = ArticleForm()
#     if request.method == "GET":
#         return render(request, "article_create.html", context={'choices': StatusChoices.choices, 'form': form})
#     form = ArticleForm(request.POST)
#     if not form.is_valid():
#         return render(request, "article_create.html", context={'choices': StatusChoices.choices, 'form': form})
#     # article_data = {
#     #     'title': request.POST.get('title'),
#     #     'author': request.POST.get('author'),
#     #     'text': request.POST.get('text')
#     # }
#     # article = Article.objects.create(**article_data)
#     article = form.save()
#     # return redirect(reverse('article-detail', kwargs={'pk': article.pk}))
#     return redirect('article_detail', pk=article.pk)
#
#
# def detail_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'article.html', context={'article': article})
#
#
#
#
#
# class ArticleUpdateView(TemplateView):
#     template_name = 'article_update.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['article'] = get_object_or_404(Article, pk=kwargs['pk'])
#         return context
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         form = ArticleForm(instance=context['article'])
#         context['form'] = form
#         return self.render_to_response(context)
#
#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs['pk'])
#         form = ArticleForm(request.POST, instance=article)
#         if form.is_valid():
#             article = form.save()
#             return redirect('article_detail', pk=article.pk)
#         return render(request, "article_update.html", context={'choices': StatusChoices.choices, 'form': form})
#
#
# def update_view(request, pk):
#     errors = {}
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         if not request.POST.get('title'):
#             errors['title'] = 'Обязательное поле'
#         article.title = request.POST.get('title')
#         article.author = request.POST.get('author')
#         article.text = request.POST.get('text')
#         article.status = request.POST.get('status')
#         if errors:
#             return render(
#                 request,
#                 'article_update.html',
#                 context={
#                     'article': article,
#                     'choices': StatusChoices.choices,
#                     'errors': errors
#                     })
#         article.save()
#         return redirect('article_detail', pk=article.pk)
#     return render(
#         request,
#         'article_update.html',
#         context={
#             'article': article,
#             'choices': StatusChoices.choices
#             })
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
