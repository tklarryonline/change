from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from income.views.add_income_view import AddIncomeView
from income.views.index_view import IndexView
from income.views.target_view import TargetView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^target$', TargetView.as_view(), name='target'),
    url(
        regex=r'^add/',
        view=login_required(AddIncomeView.as_view()),
        name='add'
    ),
]
