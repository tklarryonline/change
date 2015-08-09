import factory
from faker import Faker

from common.factories import UserFactory
from income.models.predict import IncomePredict
from income.models.records import IncomeRecord
from income.models.target import IncomeTarget


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
        django_get_or_create = ('user', )

    user = factory.SubFactory(UserFactory)
    number = factory.Sequence(lambda n: n ** 2)


class IncomeTargetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IncomeTarget

    user = factory.SubFactory(UserFactory)
    number = factory.Sequence(lambda n: n + 1)
    year = factory.Sequence(lambda n: 2010 + n)
    month = factory.Sequence(lambda n: n % 12 + 1)

