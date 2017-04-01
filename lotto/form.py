from django import forms
from .models import GuessNumbers


class PostForm1(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        # fields = ('name', 'text',)
        fields = ['name', 'text']