# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('thing', '0003_auto_20170929_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joiner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='joiners', to='users.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='joiner',
        ),
        migrations.AddField(
            model_name='join',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joins', to='thing.Trip'),
        ),
    ]
