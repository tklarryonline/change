from django.db import models
from common.models import User


class Record(models.Model):
    user_id = models.ForeignKey(to=User)
    timestamp = models.DateTimeField()
    number = models.FloatField()
