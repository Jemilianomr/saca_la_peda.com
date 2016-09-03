from django.db import models

class Car(models.Model):
	OPCIONES=[
		('recibido','Recibido'),
		('en proceso','En Proceso'),
		('atendido','Atendido'),
	]
	modelo = models.CharField(max_length=140)
	propietario = models.CharField(max_length=140)
	activo = models.BooleanField(default=True)
	issue = models.TextField()
	fecha = models.DateField(auto_now=True)
	status = models.CharField(max_length=140, choices=OPCIONES,default="recibido")
	foto = models.ImageField(upload_to='fotitos')

	def __str__(self):
		return '{} de {} estado: {}'.format(self.modelo,self.propietario,self.status)
