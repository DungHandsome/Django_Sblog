# Generated by Django 4.2.5 on 2023-11-12 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_listtruyen_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='botruyen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.listtruyen'),
        ),
    ]
