from django.db import models

class Information(models.Model):
	team_name = models.CharField(max_length=200)
	team_info = models.CharField(max_length=10000)
	image_name = models.CharField(max_length=100)
	
	def __str__(self):
		return(self.team_name)