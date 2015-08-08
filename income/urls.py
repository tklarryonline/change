from django.conf.urls import url

from income.views.add_income_view import AddIncomeView


urlpatterns = [
    url(
        regex=r'^add/',
        view=AddIncomeView.as_view(),
        name='add'
    )
]
