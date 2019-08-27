from django.db import models

from .utils import upload_location

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
	sender_id = models.CharField(max_length=255)
	logged = models.BooleanField(default=False)
	bot_service = models.BooleanField(default=True)
	balance = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s %s' % (self.name, self.last_name)