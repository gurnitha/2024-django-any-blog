# apps/marketing/models.py

# Django modules
from django.db import models

# Create your models here.

class Signup(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Singup"		
		verbose_name_plural = "Singup"		

	def __str__(self):
		return self.email

