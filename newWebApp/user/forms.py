from .models import User
from django.forms import ModelForm, TextInput, PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }