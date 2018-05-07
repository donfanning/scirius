# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-07 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0060_auto_20180403_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytransformation',
            name='key',
            field=models.CharField(choices=[(b'action', b'Action'), (b'lateral', b'Lateral'), (b'suppressed', b'Suppressed'), (b'target', b'Target')], default=b'action', max_length=15),
        ),
        migrations.AlterField(
            model_name='rulesettransformation',
            name='key',
            field=models.CharField(choices=[(b'action', b'Action'), (b'lateral', b'Lateral'), (b'suppressed', b'Suppressed'), (b'target', b'Target')], default=b'action', max_length=15),
        ),
        migrations.AlterField(
            model_name='ruletransformation',
            name='key',
            field=models.CharField(choices=[(b'action', b'Action'), (b'lateral', b'Lateral'), (b'suppressed', b'Suppressed'), (b'target', b'Target')], default=b'action', max_length=15),
        ),
    ]
