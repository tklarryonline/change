from django.db import models
from common.models import User


class IncomeRecord(models.Model):
    user = models.ForeignKey(to=User)
    timestamp = models.DateTimeField()
    number = models.FloatField(verbose_name='Income')
