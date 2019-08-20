from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	picture = models.CharField(max_length=250)
	sender_id = models.CharField(max_length=250)
	bot_service = models.BooleanField(default=False)
