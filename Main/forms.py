from django import forms
from .models import MainModel
from django.forms import Textarea,TextInput

class MainForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = "__all__"
        labels = {
            'key': 'Key:',
            'data': 'Data:'
        }
        