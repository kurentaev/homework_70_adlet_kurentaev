from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView
from webapp.models import Tasks
from webapp.forms import TasksSearchForm


class IndexView(ListView):
    template_name = 'index.html'
    model = Tasks
    context_object_name = 'tasks'
    ordering = ('-created_at',)
    paginate_by = 10
    paginate_orphans = 1
    allow_empty = False

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
        queryset = super(IndexView, self).get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

