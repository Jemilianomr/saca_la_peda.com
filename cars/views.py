from django.shortcuts import render
from django.views.generic import ListView  ##Vista de lista
from django.views.generic.detail import DetailView  ##Vista de detalle
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Car

from django.core.urlresolvers import reverse_lazy ##Nos crea un link, se usa para evitar errores a la hora de crear links

class Home(ListView):
	model = Car

class CarDetail(DetailView):
	model = Car

class CarCreation(CreateView):
	model = Car
	success_url = reverse_lazy('list')
	fields = ['modelo','propietario','issue','foto']

class CarUpdate(UpdateView):
	model = Car
	success_url = reverse_lazy('list')
	fields = ['issue','status','foto']

class CarDelete(DeleteView):
	model = Car
	success_url = reverse_lazy('list')