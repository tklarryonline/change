from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from income.forms import IncomeTargetForm
from income.models.target import IncomeTarget


class TargetView(UpdateView):
    model = IncomeTarget
    fields = ['year', 'month', 'number']
    success_url = reverse_lazy('income:index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TargetView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        target, _ = IncomeTarget.objects.get_or_create(user=self.request.user)
        return target
