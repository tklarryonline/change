from django.core.urlresolvers import reverse
from common.tests.live_server_test_case import BaseLiveTestCase


class TestViewIncomeForm(BaseLiveTestCase):

    def setUp(self):
        self.visit(page=reverse('income:add'))

    def test_view_income_form_page(self):
        self.should_see_text('Add your income record')

        self.find('#income-form').should.be.ok
        self.find('#income-form input#id_number').should.be.ok
        self.find('#income-form input#id_timestamp').should.be.ok
        self.should_see_text('Add income record')
