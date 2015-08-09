from django.core.urlresolvers import reverse
from django.db import models
from django_pandas.managers import DataFrameManager

from common.models import User


class IncomeRecord(models.Model):
    user = models.ForeignKey(to=User)
    timestamp = models.DateTimeField()
    number = models.FloatField(verbose_name='Income')
    predict_number = models.FloatField(verbose_name='Predicted Income', default=0)

    objects = DataFrameManager()

    @property
    def delete_url(self):
        return reverse('income:delete', kwargs={'pk': self.id})

    @property
    def edit_url(self):
        return reverse('income:edit', kwargs={'pk': self.id})
