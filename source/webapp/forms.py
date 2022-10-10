from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, MinLengthValidator
from django.forms import widgets
from webapp.models import Tasks, Statuses, Types


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20, message=''):
        message = 'You enter %(limit_value)s symbols %(show_value)s'
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)


class TasksListForm(forms.ModelForm):
    summary = forms.CharField(
        validators=(
            MinLengthValidator(limit_value=2, message='The task cannot be shorter than 2 characters '),
            CustomLengthValidator(limit_value=25)
        )
    )
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

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if Tasks.objects.filter(summary=summary).exists():
            raise ValidationError('Task with this summary already exists')
        return summary
