# Generated by Django 4.1.5 on 2023-01-21 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_case_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='media',
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='images/')),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.case')),
            ],
        ),
    ]