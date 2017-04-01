from django import forms

from nicekkong.models import MyNumbers


class PostForm(forms.ModelForm):

    class Meta:
        model = MyNumbers
        fields = ['name', 'status', 'level']

# class PostForm(forms.ModelForm) :
#
#     class Meta:
#         model = GuessNumbers
        ##fields = ('name', 'text',)
        # fields = ['name', 'text']