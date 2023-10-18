# Generated by Django 4.2.5 on 2023-09-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk_app', '0011_problem_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('in_progress', 'В процессе'), ('resolved', 'Решено')], default='new', max_length=20),
        ),
    ]