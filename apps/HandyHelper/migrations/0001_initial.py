# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-22 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=1000)),
                ('task_location', models.CharField(max_length=1000)),
                ('task_desc', models.CharField(max_length=100)),
                ('task_category', models.CharField(blank=True, default=False, max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_task', to='HandyHelper.User'),
        ),
        migrations.AddField(
            model_name='task',
            name='users_task_list',
            field=models.ManyToManyField(related_name='task_list', to='HandyHelper.User'),
        ),
    ]
