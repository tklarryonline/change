from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from income.views.add_income_view import AddIncomeView
from income.views.delete_view import DeleteView
from income.views.edit_view import EditView
from income.views.index_view import IndexView
from income.views.target_view import TargetView
from income.views.update_prediction_view import UpdatePredictionView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^target/$', TargetView.as_view(), name='target'),
    url(r'^delete/(?P<pk>\d*)/', DeleteView.as_view(), name='delete'),
    url(r'^edit/(?P<pk>\d*)/', EditView.as_view(), name='edit'),
    url(
        regex=r'^add/',
        view=login_required(AddIncomeView.as_view()),
        name='add'
    ),
    url(
        regex=r'^command/calculate_income_prediction/(?P<pk>\d*)/',
        view=UpdatePredictionView.as_view(),
        name='cmd_calculate_income_prediction'
    )
]
