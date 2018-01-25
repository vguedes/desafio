# coding: utf-8

"""Tests to models"""

from rest_framework import status
from rest_framework.test import (
    APIClient,
    APITestCase
)

from django.urls import reverse
from django.contrib.auth.models import User as DjangoUser

from inventory.factories import (
    ConsumerFactory,
    CountryFactory,
    StateFactory,
    CityFactory,
    CompanyFactory,
    ComplainFactory
)

from inventory.serializers import (
    CountrySerializer,
)

from inventory.models import (
    Consumer,
    Country,
    State,
    City,
    Company,
    Complain
)


class MyAPITestCase(APITestCase):
    def setUp(self):
        user = 'test'
        password = 'asdqwe123'
        self.user = DjangoUser.objects.create_superuser(
            username=user,
            password=password,
            email='a@a.co'
        )
        self.client.login(
            username=user,
            password=password
        )

        CityFactory.create_batch(2) # also creates states and countries

    def test_country_creation(self):
        country_name = 'new country'
        response = self.client.post(
            '/api/countries/',
            {'name': country_name},
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            Country.objects.get(name=country_name).name,
            country_name
        )
    
    def test_country_listing(self):
        response = self.client.get(reverse('country-list'))
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
