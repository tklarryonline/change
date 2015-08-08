from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from income.models.predict import IncomePredict

from income.models.records import IncomeRecord


class IndexView(ListView):
    queryset = IncomeRecord.objects.none()

    def get_queryset(self):
        return IncomeRecord.objects.filter(user=self.request.user).order_by('timestamp')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        incomes = context['object_list']
        incomes_length = len(incomes)

        current_number = incomes[0].number
        count_same_number = 1
        income_changes = []
        for income in incomes:
            if income.number != current_number:
                diff_number = income.number - current_number
                diff_per_month = diff_number / count_same_number
                income_changes += [diff_per_month] * count_same_number

                count_same_number = 1
                current_number = income.number
            else:
                count_same_number += 1

        context['income_changes'] = income_changes

        income_with_changes = [incomes[0].number + sum(income_changes[0:x])
                               for x in range(incomes_length - 1)]
        context['income_with_changes'] = income_with_changes

        context['income_predict'], _ = IncomePredict.objects.get_or_create(user=self.request.user)

        return context
