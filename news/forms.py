from django import forms
from .models import Categories

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Categories.objects.all())