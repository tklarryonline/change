from django.core.urlresolvers import reverse
from django.utils import timezone
from selenium.webdriver.support.select import Select

from common.tests.live_server_test_case import BaseLiveTestCase
from income.factories import IncomeTargetFactory, IncomeRecordFactory
from income.models.target import IncomeTarget


class SetIncomeTargetTestCase(BaseLiveTestCase):
    def setUp(self):
        self.login_user()

        incomes = []
        for month in range(1, 13):
            timestamp = timezone.datetime(year=2014, month=month, day=1)
            timestamp = timezone.make_aware(timestamp)
            income = IncomeRecordFactory(user=self.user, timestamp=timestamp)
            incomes.append(income)

    def test_see_button(self):
        self.visit(reverse('income:index'))

        link = self.browser.find_element_by_link_text("You haven't set target yet.")

        link.get_attribute('href').should.contain(reverse('income:target'))

    def test_set_target(self):
        self.visit(reverse('income:target'))

        self.element_for_label("Year").send_keys("2016")
        Select(self.element_for_label("Month")).select_by_visible_text('10')
        self.element_for_label("Income").send_keys("100000000")

        self.button("Set target").click()

        IncomeTarget.objects.filter(user=self.user).exists().should.be.true

        self.browser.current_url.should.contain(reverse('income:index'))

        self.should_see_text('Your next three month income should reach {next_three_months:,.0f} VND.'.format(
            next_three_months=IncomeTarget.objects.get(user=self.user).next_three_month_target()
        ))

    def test_see_target(self):
        IncomeTargetFactory(user=self.user, year=2016, month=10, number=100000000)

        self.visit(reverse('income:index'))

        self.should_see_text("Target 100,000,000 on 10/2016.")
