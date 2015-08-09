from django.core.urlresolvers import reverse
from django.utils import timezone
from common.factories import UserFactory
from common.tests.simple_test_case import SimpleTestCase
from income.factories import IncomeRecordFactory, IncomeTargetFactory


class TestUpdatePredictionView(SimpleTestCase):
    def test_get_successfully(self):
        user = UserFactory()

        incomes = []
        for month in range(1, 13):
            timestamp = timezone.datetime(year=2014, month=month, day=1)
            timestamp = timezone.make_aware(timestamp)
            income = IncomeRecordFactory(user=user, timestamp=timestamp)
            incomes.append(income)
        IncomeTargetFactory(user=user)

        response = self.client.get(reverse('income:cmd_calculate_income_prediction', args=[user.id]))
        response.status_code.should.equal(302)
        response['location'].should.contain(reverse('income:index'))
