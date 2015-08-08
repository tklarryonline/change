from django.views.generic.edit import CreateView
from income.models.records import IncomeRecord


class AddIncomeView(CreateView):
    template_name = 'income/incomerecord_form.html'
    model = IncomeRecord
    fields = ['number', 'timestamp']
