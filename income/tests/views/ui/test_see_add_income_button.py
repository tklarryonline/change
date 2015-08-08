from django.core.urlresolvers import reverse
from django.utils import timezone

from common.tests.live_server_test_case import BaseLiveTestCase
from income.factories import IncomeRecordFactory


class SeeAddIncomeTestCase(BaseLiveTestCase):
    def test_see_button(self):
        self.login_user()

        incomes = []
        for month in range(1, 13):
            timestamp = timezone.datetime(year=2014, month=month, day=1)
            timestamp = timezone.make_aware(timestamp)
            income = IncomeRecordFactory(user=self.user, timestamp=timestamp)
            incomes.append(income)

        self.incomes = incomes
        self.visit(reverse('income:index'))

        self.link("Add income").should.be.ok

        self.link("Add income").get_attribute('href').should.contain(reverse('income:add'))
