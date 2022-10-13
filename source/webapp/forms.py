from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Tasks, Statuses, Types, Projects


class TasksListForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        required=True,
        label='Status',
        queryset=Statuses.objects.all(),
        initial=[0]
    )
    type = forms.ModelMultipleChoiceField(
        required=True,
        label='Type',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    project = forms.ModelChoiceField(
        required=True,
        label='Project',
        queryset=Projects.objects.all(),
        initial=[0]
    )

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type', 'project')


class TasksSearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Task search',
    )
