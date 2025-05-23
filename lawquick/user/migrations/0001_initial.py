# Generated by Django 5.2 on 2025-04-20 19:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('marital_skipped', models.BooleanField(default=False)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('marriage_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('divorce_status', models.CharField(blank=True, max_length=50, null=True)),
                ('children_skipped', models.BooleanField(default=False)),
                ('has_children', models.BooleanField(blank=True, null=True)),
                ('children_ages', models.TextField(blank=True, null=True)),
                ('other_skipped', models.BooleanField(default=False)),
                ('property_range', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('detail_skipped', models.BooleanField(default=False)),
                ('detail_info', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
