from django import forms
from django_ace import AceWidget

from codetable.lib.utils import get_all_supported_languages
from codetable.hackerearth.parameters import SupportedLanguages


class CodeForm(forms.Form):
    text = forms.CharField(widget=AceWidget(showprintmargin=True))
    inp = forms.CharField(widget=forms.Textarea(attrs={'id': 'input'}), required=False)
    languages = [(language, language.title()) for language in get_all_supported_languages()]
    langs = forms.ChoiceField(languages, initial=SupportedLanguages.C)
