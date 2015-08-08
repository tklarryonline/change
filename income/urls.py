from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from income.views.index_view import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(
        regex=r'^add/',
        view=login_required(AddIncomeView.as_view()),
        name='add'
    ),
]
