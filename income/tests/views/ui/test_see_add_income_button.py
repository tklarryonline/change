from django.core.urlresolvers import reverse

from common.tests.live_server_test_case import BaseLiveTestCase


class SeeAddIncomeTestCase(BaseLiveTestCase):
    def test_see_button(self):
        self.login_user()
        self.visit(reverse('income:index'))

        self.link("Add income").should.be.ok

        self.link("Add income").get_attribute('href').should.contain(reverse('income:add'))
