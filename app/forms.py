from django import forms
from django.forms import widgets
from . import models

class MainForm(forms.ModelForm):
    class Meta:
        model = models.Main
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'your task...'})
        }