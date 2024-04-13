# Generated by Django 5.0.3 on 2024-03-07 14:00

import cloud_api.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('file_file', models.FileField(blank=True, null=True, upload_to=cloud_api.models.user_directory_path)),
                ('file_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('size_file', models.CharField(blank=True, max_length=50)),
                ('last_download_time', models.DateTimeField(null=True)),
                ('file_type', models.CharField(blank=True, max_length=20, null=True)),
                ('id_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
