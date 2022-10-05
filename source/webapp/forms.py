from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
# from webapp.models import StatusChoices
#
#
# class TasksListForm(forms.Form):
#     title = forms.CharField(max_length=400, required=True, label='Title')
#     status = forms.ChoiceField(required=True, label='Status', choices=StatusChoices.choices)
#     deadline = forms.DateField(required=False,
#                                label='Deadline',
#                                widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     description = forms.CharField(max_length=3000,
#                                   required=False,
#                                   label='Description',
#                                   widget=widgets.Textarea)
#
#     def clean_title(self):
#         title = self.cleaned_data.get('title')
#         if len(title) < 1:
#             raise ValidationError('The title must be longer than one characters')
#         return title
