# Generated by Django 4.1.1 on 2023-04-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_section_article_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, upload_to='articles/documents/'),
        ),
    ]