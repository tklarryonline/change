from datetime import timedelta
from dateutil import relativedelta
from django.db import models
from django.utils import timezone
from django_extensions.db.fields.json import JSONField
import numpy as np

from common.models import User


MONTH_CHOICES = zip(range(1, 13), range(1, 13))


class IncomeTarget(models.Model):
    user = models.OneToOneField(User)
    number = models.FloatField(verbose_name='Income', default=0)
    year = models.IntegerField(default=0)
    month = models.IntegerField(choices=MONTH_CHOICES, default=1)
    coeffs = JSONField(default=[])

    def next_three_month_target(self):
        polyfit = np.poly1d([float(x) for x in self.coeffs])
        three_month = timezone.now() + relativedelta.relativedelta(months=3)
        return polyfit(three_month.timestamp() / 1e3)
