# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cours_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
    ]
