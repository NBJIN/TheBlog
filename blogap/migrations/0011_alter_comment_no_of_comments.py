# Generated by Django 3.2.16 on 2023-02-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogap', '0010_alter_comment_date_of_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='no_of_comments',
            field=models.ManyToManyField(related_name='blog_comment', to='blogap.Post'),
        ),
    ]
