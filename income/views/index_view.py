from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from income.models.records import IncomeRecord


class IndexView(ListView):
    queryset = IncomeRecord.objects.none()

    def get_queryset(self):
        return IncomeRecord.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)
