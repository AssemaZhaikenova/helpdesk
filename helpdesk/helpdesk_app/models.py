from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

reception_group, created = Group.objects.get_or_create(name='Reception')
tester_group, created = Group.objects.get_or_create(name='Tester')


PRIORITY_CHOICES = [
    ('low', 'Низкий'),
    ('medium', 'Средний'),
    ('high', 'Высокий'),
]

STATUS_CHOICES = [
    ('new', 'Новый'),
    ('in_progress', 'В процессе'),
    ('resolved', 'Решено'),
    ('confirmed', 'Подтверждено'),
]


class Problem(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    actions = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_problems')
    resolved_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_problems')
