# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from main.models import Cours

def home(request):
	formations = Cours.objects.all()
	return render(request, 'monCV/home.html', locals())

def afficher_cours(request, cours_id):
	""" Afficher un cours"""
	cours = get_object_or_404(Cours, id=cours_id)
	formations = Cours.objects.all()
	return render(request, 'monCV/afficher_cours.html', locals())
