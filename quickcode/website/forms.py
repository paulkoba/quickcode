from django import forms
from .models import LANGUAGE


class SubmissionForm(forms.Form):
    file = forms.FileField(label="")
    language = forms.ChoiceField(choices=LANGUAGE, label="", widget=forms.Select())
