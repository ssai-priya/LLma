# Generated by Django 4.1.10 on 2023-09-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeBridge_Backend', '0005_mermaiddiagrams'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='code_language',
            field=models.CharField(max_length=50, null=True),
        ),
    ]