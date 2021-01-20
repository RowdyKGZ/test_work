import datetime

from django.db import models


class TargetUrl(models.Model):
    url = models.CharField(max_length=100)

    def result(self):

class Results(models.Model):
    h1 = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    meta = models.CharField(max_length=255)
