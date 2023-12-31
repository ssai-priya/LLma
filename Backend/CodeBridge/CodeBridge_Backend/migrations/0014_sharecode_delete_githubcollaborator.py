# Generated by Django 4.1.11 on 2023-10-25 03:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CodeBridge_Backend', '0013_javacode_language_converted_javacode_repository'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('folder_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CodeBridge_Backend.folderupload')),
                ('users', models.ManyToManyField(related_name='shared_links', to='CodeBridge_Backend.user')),
            ],
        ),
        migrations.DeleteModel(
            name='GitHubCollaborator',
        ),
    ]
