from django.db import models

from common.models import User


class IncomePredict(models.Model):
    user = models.OneToOneField(to=User)
    number = models.FloatField(verbose_name='Income', default=0)
