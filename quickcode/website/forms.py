from django import forms
from django.utils.translation import gettext_lazy as _

LANGUAGE = (
    (1, _("CPP")),
)


class SubmissionForm(forms.Form):
    file = forms.FileField(label="")
    language = forms.ChoiceField(choices=LANGUAGE, label="", widget=forms.Select())
