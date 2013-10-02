# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeClass(TemplateView):

	template_name = "home.html"

class SobreClass(TemplateView):

	template_name = "sobre.html"

class ContatoClass(TemplateView):

	template_name = "contato.html"