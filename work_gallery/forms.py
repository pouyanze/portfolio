from django import forms
from .models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'autofocus': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }