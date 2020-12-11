from django.db import models


class ExchangeRate(models.Model):
    name = models.CharField(max_length=3)
    rate = models.FloatField()
    date = models.DateField()
