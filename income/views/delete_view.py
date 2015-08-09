from django.core.urlresolvers import reverse_lazy
from django.http.response import Http404
from django.views.generic.edit import DeleteView as BaseDeleteView

from income.models.records import IncomeRecord


class DeleteView(BaseDeleteView):
    model = IncomeRecord
    success_url = reverse_lazy('income:index')

    def get_object(self):
        obj = super(DeleteView, self).get_object()
        if obj.user.pk != self.request.user.pk:
            raise Http404()
        return obj
