from django.views.generic import TemplateView
from webapp.models import Tasks


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all().order_by('-summary')
        return context
