# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='link',
            field=models.CharField(max_length=255, blank=True, null=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='path',
            field=models.CharField(max_length=255, blank=True, null=True, help_text=''),
        ),
    ]
