# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='categorie',
            field=models.ForeignKey(default=1, to='main.Categorie'),
            preserve_default=True,
        ),
    ]
