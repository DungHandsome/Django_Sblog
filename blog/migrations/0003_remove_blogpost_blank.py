# Generated by Django 4.2.5 on 2023-11-12 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_blank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='blank',
        ),
    ]