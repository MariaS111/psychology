# Generated by Django 4.1.1 on 2023-04-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='section',
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ManyToManyField(to='articles.section'),
        ),
    ]
