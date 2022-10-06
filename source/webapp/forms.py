from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Tasks, Statuses, Types


class TasksListForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=False, label='Status', queryset=Statuses.objects.all())
    type = forms.ModelChoiceField(required=False, label='Type', queryset=Types.objects.all())

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')

    def clean_title(self):
        title = self.cleaned_data.get('summary')
        if len(title) < 1:
            raise ValidationError('The title must be longer than one characters')
        return title
