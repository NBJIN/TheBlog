# Generated by Django 3.2.16 on 2023-02-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogap', '0009_alter_comment_date_of_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_of_comment',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]