from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from income.models.records import IncomeRecord


class AddIncomeView(CreateView):
    template_name = 'income/incomerecord_form.html'
    model = IncomeRecord
    fields = ['number', 'timestamp']
    success_url = reverse_lazy('income:add')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddIncomeView, self).form_valid(form)
