# Generated by Django 3.2.16 on 2023-02-04 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogap', '0020_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
