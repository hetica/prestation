# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_categorie', models.CharField(max_length=30)),
                ('libelle', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
