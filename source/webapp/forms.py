from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Tasks


class TasksListForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')

    def clean_title(self):
        title = self.cleaned_data.get('summary')
        if len(title) < 1:
            raise ValidationError('The title must be longer than one characters')
        return title
