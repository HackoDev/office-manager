# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-22 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
                ('author', models.CharField(max_length=256, verbose_name='author')),
                ('publisher', models.CharField(max_length=256, verbose_name='publisher')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('specializations', models.ManyToManyField(blank=True, related_name='books', to='employees.Specialization', verbose_name='specializations')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, default='', verbose_name='notes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('refunded_at', models.DateTimeField(blank=True, null=True, verbose_name='refunded at')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holder_history', to='library.Book', verbose_name='book')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holder_history', to='employees.Employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'holder',
                'verbose_name_plural': 'holders',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', max_length=512, verbose_name='url')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('book', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='library.Book', verbose_name='book')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_offers', to='employees.Employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'offer',
                'verbose_name_plural': 'offer',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='books', to='library.Tag', verbose_name='tags'),
        ),
    ]
