from django import forms
from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'category',
            'image',
            'image_by',
            'tags'
        ]
