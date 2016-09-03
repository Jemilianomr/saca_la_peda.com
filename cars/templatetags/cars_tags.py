from django import template
from ..models import Car

register = template.Library()

@register.simple_tag(name='problemasTotales')
def total_issues():
	return Car.objects.all().count()

@register.simple_tag
def propietario():
	return Car.objects.get(id=1).propietario

@register.inclusion_tag('cars/tag.html')
def ultimo (count=2):
	ultimosIssues=Car.objects.all().order_by('-fecha')[:count]
	return{'ultimosIssues':ultimosIssues}

@register.assignment_tag
def ultimos(count=2):
	return Car.objects.all().order_by('-fecha')[count:]

@register.inclusion_tag('cars/recibido.html')
def recibidos():
	recibidos=Car.objects.filter(status='recibido')
	return{'recibidos':recibidos}