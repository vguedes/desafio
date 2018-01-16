from rest_framework import serializers
from inventory.models import (
    Country,
    State,
    City,
    Consumer,
    Company,
    Complain
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name', 'country')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'state')


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'name', 'email')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'city')


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = (
            'id',
            'consumer',
            'city',
            'company',
            'datetime',
            'title',
            'description'
        )
