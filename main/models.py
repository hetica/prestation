# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Cours(models.Model):
	id_cours = models.CharField(max_length=25)
	intitule = models.CharField(max_length=100)
	prerequis = models.TextField(default="Aucun")
	objectif = models.TextField(default="")
	duree = models.IntegerField(max_length=2)
	icone = models.CharField(max_length=25, null=True)
	categorie = models.ForeignKey('Categorie', default=1)
	mots_cles = models.CharField(max_length=100, null=True)
	tarif = models.IntegerField(max_length=4)
	contenu = models.TextField()
	
	def __str__(self):
		"""
                Cette méthode à définir dans tous les modèles permettra
		de reconnaître facilement les différents objets traités
                par la suite et pour l'administration
                """
                return u'%s' % self.id_cours

class Categorie(models.Model):
	id_categorie = models.CharField(max_length=30)
	libelle = models.CharField(max_length=45)

	def __str__(self):
		return u'%s' % self.id_categorie
