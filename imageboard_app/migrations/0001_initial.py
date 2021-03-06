# Generated by Django 3.0.7 on 2020-07-07 08:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='imageboard/posts/')),
                ('subject', models.TextField(max_length=40)),
                ('description', models.TextField(max_length=600)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='imageboard_app.Post')),
            ],
            options={
                'verbose_name_plural': 'replies',
            },
        ),
    ]
