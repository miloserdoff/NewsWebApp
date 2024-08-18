from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
import datetime

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']
        current_time = datetime.datetime.now()
        current_time_to_field = f'{current_time.year}-{current_time.month}-{current_time.day} {current_time.hour}:{current_time.minute}:{current_time.second}'
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'value': current_time_to_field,
                'readonly': True
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Статья'
            })
        }