# Generated by Django 3.2.16 on 2023-02-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogap', '0017_alter_comment_contributor_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cname',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
