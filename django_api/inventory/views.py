from inventory.models import (
    Country,
    State,
    City,
    Consumer,
    Company,
    Complain
)
from inventory.serializers import (
    CountrySerializer,
    StateSerializer,
    CitySerializer,
    ConsumerSerializer,
    CompanySerializer,
    ComplainSerializer
)
from rest_framework import viewsets


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class ConsumerViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumerSerializer
    queryset = Consumer.objects.all()


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ComplainViewSet(viewsets.ModelViewSet):
    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()
