# Generated by Django 4.1 on 2024-02-14 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidaytrip',
            name='holiday_tyoe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='holiday.holidaytype'),
        ),
    ]