from django.core.management.base import BaseCommand

import numpy as np
import pandas as pd

from income.models.records import IncomeRecord


class Command(BaseCommand):
    help = 'Calculate and update the predicted income'

    def handle(self, *args, **options):
        income_records = IncomeRecord.objects.all().to_dataframe()
        income_records = income_records.sort(columns=['timestamp']).reset_index(drop=True)

        # Converts timestamp to int, then divides them by trillion since they would be too big
        income_records['timestamp_float'] = pd.to_datetime(income_records['timestamp'], utc=True).astype(int) / 1e12

        # Calculates polyfit
        x = income_records['timestamp_float']
        y = income_records['number']
        fit = np.polyfit(x, y, 2)
        polyfit = np.poly1d(fit)

        income_records['predict_number'] = polyfit(x)

        for index, row in income_records.iterrows():
            income_record = IncomeRecord.objects.get(pk=row['id'])
            income_record.predict_number = row['predict_number']
            income_record.save()
