# Generated by Django 2.2.5 on 2020-03-10 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat_messages', '0006_auto_20200310_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время создания'),
        ),
    ]