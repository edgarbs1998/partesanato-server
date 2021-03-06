# Generated by Django 2.0.1 on 2018-01-29 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=2000)),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='image_height', upload_to=posts.models.image.post_directory_path, width_field='image_width')),
                ('image_width', models.IntegerField()),
                ('image_height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(max_length=6000)),
                ('approved', models.BooleanField(default=False, help_text='Designates whether this post will be visible to regular users.')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='posted by')),
            ],
            options={
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='image', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='commented by'),
        ),
    ]
