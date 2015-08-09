from django.core.urlresolvers import reverse
from common.factories import UserFactory
from common.tests.live_server_test_case import BaseLiveTestCase

from income.models.records import IncomeRecord


class TestViewIncomeForm(BaseLiveTestCase):

    def setUp(self):
        self.user = UserFactory()
        self.login(self.user)
        self.visit(page=reverse('income:add'))

    def test_view_income_form_page(self):
        self.should_see_text('Add your income record')

        self.find('#income-form').should.be.ok
        self.find('#income-form #id_number').should.be.ok
        self.find('#income-form #id_timestamp').should.be.ok
        self.should_see_text('Save income')

    def test_add_income_page(self):
        num_records = IncomeRecord.objects.count()
        self.fill_in(selector='#id_number', value='10000')
        self.fill_in(selector='#id_timestamp', value='2015-06-28')
        self.button('Save income').click()
        IncomeRecord.objects.count().should.equal(num_records + 1)
