from django.core.urlresolvers import reverse
from common.tests.simple_test_case import SimpleTestCase


class TestAddIncomeView(SimpleTestCase):
    def test_login_required(self):
        response = self.client.get(reverse('income:add'))
        response.status_code.should.equal(302)
        response['location'].should.contain(reverse('accounts:login'))