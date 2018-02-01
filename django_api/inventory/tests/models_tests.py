# coding: utf-8

"""Tests to models"""

from django.test import TestCase

from inventory.factories import (
    ConsumerFactory,
    CountryFactory,
    StateFactory,
    CityFactory,
    CompanyFactory,
    ComplainFactory
)

from inventory.models import (
    Consumer,
    Country,
    State,
    City,
    Company
)

### IMPORTANT ###
# Model atributes testing enforced by Meta class (fields attribute) of serializers


class CountryModelTestCase(TestCase):
    def test_model(self):
        countries_to_create = 2
        CountryFactory.create_batch(countries_to_create)

        self.assertEqual(countries_to_create, Country.objects.count())


class StateModelTestCase(TestCase):
    def test_country_relation(self):
        state = StateFactory.create()

        self.assertEqual(isinstance(state.country, Country), True)


class CityModelTestCase(TestCase):
    def test_state_relation(self):
        city = CityFactory.create()

        self.assertEqual(isinstance(city.state, State), True)


class ConsumerModelTestCase(TestCase):
    def test_model(self):
        consumers_to_create = 2
        ConsumerFactory.create_batch(consumers_to_create)

        self.assertEqual(consumers_to_create, Consumer.objects.count())


class CompanyModelTestCase(TestCase):
    def test_city_relation(self):
        company = CompanyFactory.create()

        self.assertEqual(isinstance(company.city, City), True)


class ComplainModelTestCase(TestCase):
    def test_fk_relations(self):
        complain = ComplainFactory.create()

        self.assertEqual(isinstance(complain.consumer, Consumer), True)
        self.assertEqual(isinstance(complain.city, City), True)
        self.assertEqual(isinstance(complain.company, Company), True)
