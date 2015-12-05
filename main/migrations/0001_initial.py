# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cours', models.CharField(max_length=25)),
                ('intitule', models.CharField(max_length=100)),
                ('prerequis', models.TextField(default=b'Aucun')),
                ('objectif', models.TextField(default=b'')),
                ('duree', models.IntegerField(max_length=2)),
                ('icone', models.CharField(max_length=25, null=True)),
                ('categorie', models.CharField(max_length=45, null=True)),
                ('mots_cles', models.CharField(max_length=100, null=True)),
                ('tarif', models.IntegerField(max_length=4)),
                ('contenu', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
