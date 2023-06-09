# Generated by Django 4.2 on 2023-05-07 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('psychologists', '0010_rename_comment_commentuserpsychologist'),
        ('articles', '0006_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('psychologist', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='psychologists.psychologist')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
