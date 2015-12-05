# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141119_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='categorie',
        ),
    ]
