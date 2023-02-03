# Generated by Django 3.2.16 on 2023-02-03 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogap', '0014_auto_20230203_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
