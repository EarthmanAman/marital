# Generated by Django 4.1.5 on 2023-05-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
            ],
        ),
    ]
