# Generated by Django 4.1.5 on 2023-01-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='status',
        ),
        migrations.AddField(
            model_name='case',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
