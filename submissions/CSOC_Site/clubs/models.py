from django.db import models


class clubs(models.Model):
	club_name = models.CharField(max_length=200)
	club_content = models.CharField(max_length=10000)
	club_link = models.CharField(max_length=200)
	club_image_name = models.CharField(max_length=200)

	def __str__(self):
		return(self.club_name)

