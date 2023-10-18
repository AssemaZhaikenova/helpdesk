from django import forms
from django.contrib.auth.models import User
from .models import Problem


class ProblemForm(forms.ModelForm):
    reception_user = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='Reception'),
        required=False,
        widget=forms.Select,
        label='Перенаправить заявку в группу Reception'
    )

    class Meta:
        model = Problem
        fields = ['name', 'phone', 'email', 'description', 'priority', 'assigned_user', 'reception_user']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Email',
            'description': 'Описание',
            'priority': 'Приоритет',
            'assigned_user': 'Назначенный пользователь',
        }
