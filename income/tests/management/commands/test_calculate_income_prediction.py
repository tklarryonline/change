from django.core.management import call_command
from django.test.testcases import TestCase
from django.utils import timezone

from common.factories import UserFactory
from income.factories import IncomeRecordFactory, IncomeTargetFactory
from income.models.predict import IncomePredict


class TestCalculateIncomePredictionCommand(TestCase):

    def setUp(self):
        self.user = UserFactory()

        incomes = []
        for month in range(1, 13):
            timestamp = timezone.datetime(year=2014, month=month, day=1)
            timestamp = timezone.make_aware(timestamp)
            income = IncomeRecordFactory(user=self.user, timestamp=timestamp)
            incomes.append(income)

        IncomeTargetFactory(user=self.user)

    def test_call_command_success(self):
        predict_num = IncomePredict.objects.count()
        call_command('calculate_income_prediction', uid=self.user.id)

        IncomePredict.objects.count().should.equal(predict_num + 1)

    def test_call_command_fail(self):
        predict_num = IncomePredict.objects.count()
        call_command('calculate_income_prediction')
        IncomePredict.objects.count().should.equal(predict_num)
