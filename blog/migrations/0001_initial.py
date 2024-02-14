# Generated by Django 4.1 on 2024-02-14 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, default='', max_length=150)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
                ('contents', models.TextField(blank=True, default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='site/images')),
            ],
        ),
    ]