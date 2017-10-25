from django.db import models
from rest_framework import serializers

class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    style = models.CharField(default='friendly', max_length=100)

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'linenos', 'language', 'style')