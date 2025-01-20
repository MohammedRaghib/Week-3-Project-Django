from django import forms
from .models import Post

class PostCreation(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'photo']