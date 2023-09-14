# Generated by Django 4.2.1 on 2023-07-04 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CodeBridge_Backend', '0004_alter_fileupload_file_logic_javacode'),
    ]

    operations = [
        migrations.CreateModel(
            name='MermaidDiagrams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classDiagram', models.TextField()),
                ('flowChart', models.TextField()),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CodeBridge_Backend.fileupload')),
                ('logic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CodeBridge_Backend.logic')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CodeBridge_Backend.user')),
            ],
        ),
    ]