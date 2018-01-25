# coding: utf-8

"""Tests to models"""

import json
import datetime

from freezegun import freeze_time

from rest_framework import status
from rest_framework.test import (
    APITestCase
)

from django.urls import reverse
from django.contrib.auth.models import User as DjangoUser

from inventory.factories import (
    CityFactory,
    ComplainFactory
)

from inventory.serializers import (
    CountrySerializer,
    ComplainSerializer
)

from inventory.models import (
    Country,
    Complain
)


class CountryAPITestCase(APITestCase):
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

    def test_valid_creation(self):
        country_name = 'new country'
        response = self.client.post(
            reverse('country-list'),
            data=json.dumps({'name': country_name}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            Country.objects.get(name=country_name).name,
            country_name
        )

    def test_invalid_creation(self):
        response = self.client.post(
            reverse('country-list'),
            data=json.dumps({'name': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listing(self):
        response = self.client.get(reverse('country-list'))
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_retival(self):
        country = Country.objects.first()
        response = self.client.get(
            reverse('country-detail', kwargs={'pk': country.id})
        )
        serializer = CountrySerializer(country)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_retival(self):
        response = self.client.get(
            reverse('country-detail', kwargs={'pk': 2018})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update(self):
        country = Country.objects.first()
        response = self.client.put(
            reverse('country-detail', kwargs={'pk': country.id}),
            data=json.dumps({'name': 'Changed'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update(self):
        country = Country.objects.first()
        response = self.client.put(
            reverse('country-detail', kwargs={'pk': country.id}),
            data=json.dumps({'name': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_deletion(self):
        country = Country.objects.first()
        response = self.client.delete(
            '/api/countries/{}'.format(country.id)
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_invalid_deletion(self):
        response = self.client.delete(
            reverse('country-detail', kwargs={'pk': 2018}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


""" TODO: DO FOR ALL OTHER MODEL OBJECTS
class StateAPITestCase(APITestCase):
class CityAPITestCase(APITestCase):
class ConsumerAPITestCase(APITestCase):
class CompanyAPITestCase(APITestCase):
class ComplainAPITestCase(APITestCase):
"""


@freeze_time("2018-01-25")
class CustomComplainByCreatedRange(APITestCase):
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

        ComplainFactory.create_batch(4)

    def test_listing_with_data(self):
        response = self.client.get(
            '/api/complains/?created_min=2018-01-24;created_max=2018-01-25'
        )
        complains = Complain.objects.all()
        serializer = ComplainSerializer(complains, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_without_data(self):
        response = self.client.get(
            '/api/complains/?created_min=2001-01-01;created_max=2001-01-02'
        )
        self.assertEqual(response.data['results'], [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_parameter_created_min_only(self):
        complain = ComplainFactory.create()
        complain.created = datetime.date(2018, 1, 26)
        complain.save()
        response = self.client.get('/api/complains/?created_min=2018-01-26')
        complains = Complain.objects.filter(created='2018-01-26')
        serializer = ComplainSerializer(complains, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_parameter_created_max_only(self):
        complain = ComplainFactory.create()
        complain.created = datetime.date(2018, 1, 26)
        complain.save()
        response = self.client.get('/api/complains/?created_max=2018-01-25')
        complains = Complain.objects.filter(created__lt='2018-01-26')
        serializer = ComplainSerializer(complains, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
