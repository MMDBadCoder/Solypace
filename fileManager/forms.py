from django import forms
from django.core.exceptions import ValidationError

from fileManager.models import SolyFile, SuggestedFile


class FileForm(forms.ModelForm):
    class Meta:
        model = SolyFile
        fields = ('description', 'label', 'parent', 'url')


class SuggestedFileForm(forms.ModelForm):
    class Meta:
        model = SuggestedFile
        fields = ('author_name', 'author_email', 'description', 'file')
