from django.db import models

from common.models import User


MONTH_CHOICES = zip(range(1, 13), range(1, 13))


class IncomeTarget(models.Model):
    user = models.OneToOneField(User)
    number = models.FloatField(verbose_name='Income', default=0)
    year = models.IntegerField(default=0)
    month = models.IntegerField(choices=MONTH_CHOICES, default=1)
