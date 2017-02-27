# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_poke'),
    ]

    operations = [
        migrations.AddField(
            model_name='poke',
            name='aggressor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='main.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poke',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='main.User'),
        ),
    ]