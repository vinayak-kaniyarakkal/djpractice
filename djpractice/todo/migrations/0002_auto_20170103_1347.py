# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveIntegerField(default=1, choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.PositiveIntegerField(default=0, choices=[(0, 'ToDo'), (1, 'Doing'), (2, 'Done')]),
            preserve_default=True,
        ),
    ]
