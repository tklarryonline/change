import factory
from faker import Faker

from common.factories import UserFactory
from income.models.records import IncomeRecord


fake = Faker()


class IncomeRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IncomeRecord

    user = factory.SubFactory(UserFactory)
    timestamp = factory.Sequence(lambda n: fake.date_time())
    number = factory.Sequence(lambda n: n + 1)
