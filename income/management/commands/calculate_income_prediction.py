from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

import numpy as np
import pandas as pd

from common.models import User
from income.models.predict import IncomePredict
from income.models.records import IncomeRecord


class Command(BaseCommand):
    help = 'Calculate and update the predicted income'

    def add_arguments(self, parser):
        parser.add_argument('--uid',
                            help='User ID')

    @staticmethod
    def get_polyfit(income_records):
        # Calculates polyfit
        x = income_records['timestamp_float']
        y = income_records['number']
        fit = np.polyfit(x, y, 2)
        return np.poly1d(fit)

    def timestamp_to_int(self, timestamp):
        return timestamp.value / 1e12

    def handle(self, uid, **options):
        if not uid:
            print('User id is required')
            return

        user = User.objects.get(pk=uid)
        income_records = user.incomerecord_set.to_dataframe()
        income_records = income_records.sort(columns=['timestamp']).reset_index(drop=True)

        # Converts timestamp to int, then divides them by trillion since they would be too big
        income_records['timestamp_float'] = pd.to_datetime(income_records['timestamp'], utc=True).astype(int) / 1e12

        # Calculates polyfit
        x = income_records['timestamp_float']
        polyfit = self.get_polyfit(income_records)

        income_records['predict_number'] = polyfit(x)

        for index, row in income_records.iterrows():
            income_record = IncomeRecord.objects.get(pk=row['id'])
            income_record.predict_number = row['predict_number']
            income_record.save()

        # Calculates next year value
        next_year = pd.Timestamp(timezone.now() + relativedelta(years=1))
        next_year = self.timestamp_to_int(next_year)

        income_predict, created = IncomePredict.objects.get_or_create(user=user)

        income_predict.number = polyfit(next_year)
        income_predict.save()

        # calculate with target
        income_target = user.incometarget
        timestamp = pd.Timestamp(timezone.datetime(year=income_target.year, month=income_target.month, day=1))
        income_records = income_records.append([{
            'timestamp_float': self.timestamp_to_int(timestamp),
            'number': income_target.number,
        }])
        new_polyfit = self.get_polyfit(income_records)
        income_target.coeffs = new_polyfit.coeffs.tolist()
        income_target.save()
