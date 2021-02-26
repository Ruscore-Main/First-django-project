from django import forms
from .models import Categories

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст:', required=False,  widget=forms.Textarea(attrs={'class': 'form-control'}))
    #initial - начальное значение, required - обязательное ли поле
    is_published = forms.BooleanField(label='Опубликовать?:', initial=False, required=False)
    # empty_label - нач знач выпадающего списка, по умолчанию -------
    category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Categories.objects.all(), label='Категория:', required=False, widget=forms.Select(attrs={'class': 'form-control'}))