# Generated by Django 4.2 on 2023-05-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologists', '0007_psychologist_is_psychologist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychologist',
            name='is_psychologist',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_psychologist',
            field=models.BooleanField(default=True),
        ),
    ]
