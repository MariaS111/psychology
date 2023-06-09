# Generated by Django 4.2 on 2023-05-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologists', '0012_alter_session_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('await_confirmation', 'Waiting for confirmation'), ('await', 'Await'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='await_confirmation', max_length=20),
        ),
    ]
