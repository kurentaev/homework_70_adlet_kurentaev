from django import forms
from django.forms import widgets
from webapp.models import Tasks, Statuses, Types


class TasksListForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        required=True,
        label='Status',
        queryset=Statuses.objects.all()
    )

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')
        widgets = {
            'type': widgets.CheckboxSelectMultiple
        }
