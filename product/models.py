from django.db import models

# Create your models here.

class Product(models.Model):
	Name          = models.CharField(max_length = 100, default=None)
	Description   = models.TextField(default=None)
	CostPerItem   = models.IntegerField(default=None) 
	StockQuantity = models.IntegerField(default=None)
	Volume        = models.IntegerField(editable=False,blank=True)
		
	
	def __str__(self):
		return self.Name
