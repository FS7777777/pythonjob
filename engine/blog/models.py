from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    """docstring for Question"""
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date pubiselished')


class Choise(models.Model):
    """docstring for Cho"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
