# Generated by Django 3.2.16 on 2023-02-04 13:42

import ckeditor.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogap', '0022_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contributor_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AddPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_post', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('update_post', models.DateTimeField(auto_now_add=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=7000, null=True)),
                ('excerpt', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('no_of_likes', models.ManyToManyField(related_name='blogap_no_of_likes', to=settings.AUTH_USER_MODEL)),
                ('post_contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
