from django.db import models

class Player(models.Model):
	nickname=models.CharField(max_length=63)
	real_name=models.CharField(max_length=63)
	real_surname=models.CharField(max_length=63)
	nationality=models.CharField(max_length=31)
	team=models.CharField(max_length=31)
	region=models.CharField(max_length=31)
	next_match_date=models.CharField(max_length=31, default = 'Неизвестно')
	next_match_url=models.CharField(max_length=255, default = 'https://www.twitch.tv/rainbow6')

	class Meta:
		verbose_name_plural="players"

	def __str__(self):
		return self.nickname

