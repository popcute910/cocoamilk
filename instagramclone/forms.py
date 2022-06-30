from django import forms

from .models import Instapost

class PostForm(forms.ModelForm):

    class Meta:
        model = Instapost
        fields = ('text',)