from django.conf.urls import url

from income.views.index_view import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
