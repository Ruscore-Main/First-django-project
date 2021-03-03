from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
# Не связанная с моделью
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название:', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Текст:', required=False,  widget=forms.Textarea(attrs={'class': 'form-control'}))
#     #initial - начальное значение, required - обязательное ли поле
#     is_published = forms.BooleanField(label='Опубликовать?:', initial=False, required=False)
#     # empty_label - нач знач выпадающего списка, по умолчанию -------
#     category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Categories.objects.all(), label='Категория:',required=False, widget=forms.Select(attrs={'class': 'form-control'}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # все поля: fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    #Собственный валидатор
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title