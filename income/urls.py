from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from income.views.add_income_view import AddIncomeView


urlpatterns = [
    url(
        regex=r'^add/',
        view=login_required(AddIncomeView.as_view()),
        name='add'
    )
]
