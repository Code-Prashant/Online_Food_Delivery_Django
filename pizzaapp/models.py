from django.db import models

class PizzaModel(models.Model):
	name = models.CharField(max_length = 10)
	price = models.CharField(max_length = 10)

class CustomerModal(models.Model):
	userid = models.CharField(max_length = 10)
	phone = models.CharField(max_length = 10)

class OrderdModel(models.Model):
	username = models.CharField(max_length = 10)
	phone = models.CharField(max_length = 10)
	address = models.CharField(max_length = 10)
	ordereditem = models.CharField(max_length = 10)
	status = models.CharField(max_length = 10)