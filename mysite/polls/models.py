# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible 	#As the python version I'm using is 2.7
# Create your models here.
class Question(models.Model):
	question_text= models.CharField(max_length=200)
	pub_date= models.DateTimeField('data published')
	
	def __str__(self):
		return self.question_text
		
	def was_published_recently(self):
		now=timezone.now()
	        return now-datetime.timedelta(days=1)<=self.pub_date<=now

class Choice(models.Model):
	question= models.ForeignKey(Question, on_delete= models.CASCADE)
	choice_text= models.CharField(max_length=200)
	votes= models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text