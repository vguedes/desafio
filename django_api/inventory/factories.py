#coding: utf-8

import factory
from inventory.models import (
    Consumer,
    Complain,
    Company,
    Country,
    State,
    City
)


class CountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Country
    
    name = factory.Sequence(lambda x: 'Country %d' % x)


class StateFactory(factory.DjangoModelFactory):
    class Meta:
        model = State
    
    name = factory.Sequence(lambda x: 'State %d' % x)
    country = factory.SubFactory(CountryFactory)


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City
    
    name = factory.Sequence(lambda x: 'City %d' % x)
    state = factory.SubFactory(StateFactory)


class ConsumerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Consumer
    
    name = factory.Sequence(lambda x: 'Consumer %d' % x)
    email = factory.Sequence(lambda x: 'consumer%d@domain.org' % x)


class CompanyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Sequence(lambda x: 'Company %d' % x)
    city = factory.SubFactory(CityFactory)


class ComplainFactory(factory.DjangoModelFactory):
    class Meta:
        model = Complain
    
    title = factory.Sequence(lambda x: 'Title %d' % x)
    description = factory.Sequence(lambda x: 'Description %d' % x)
    consumer = factory.SubFactory(ConsumerFactory)
    city = factory.SubFactory(CityFactory)
    company = factory.SubFactory(CompanyFactory)
