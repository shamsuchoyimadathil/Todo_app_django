from django import forms
from . import models

class MainForm(forms.ModelForm):
    class Meta:
        model = models.Main
        fields = "__all__"

