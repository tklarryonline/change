from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from django.utils import timezone

from common.tests.live_server_test_case import BaseLiveTestCase
from income.factories import IncomeRecordFactory


class ViewIncomeChartTestCase(BaseLiveTestCase):
    def test_user_see_chart(self):
        self.init_user()

        incomes = []
        for month in range(1, 13):
            timestamp = timezone.datetime(year=2014, month=month, day=1)
            timestamp = timezone.make_aware(timestamp)
            income = IncomeRecordFactory(user=self.user, timestamp=timestamp)
            incomes.append(income)

        self.login_user()

        self.visit(reverse('income:index'))

        self.find("#income-chart").should.be.ok

        for income in incomes:
            self.should_see_text(date(income.timestamp, settings.SHORT_DATE_FORMAT))

        chart = self.find("#income-chart")
        chart.size['height'].shouldnt.equal(0)
