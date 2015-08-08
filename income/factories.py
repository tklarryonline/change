import factory
from faker import Faker

from common.factories import UserFactory
from income.models.predict import IncomePredict
from income.models.records import IncomeRecord


fake = Faker()


class IncomeRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IncomeRecord

    user = factory.SubFactory(UserFactory)
    timestamp = factory.Sequence(lambda n: fake.date_time())
    number = factory.Sequence(lambda n: n + 1)


class IncomePredictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IncomePredict

    user = factory.SubFactory(UserFactory)
    number = factory.Sequence(lambda n: n ** 2)
