"""API Views"""

from rest_framework import viewsets
from rest_framework import permissions
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


class IsAuthenticated():
    permission_classes = (permissions.IsAuthenticated,)


class CountryViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class StateViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class CityViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class ConsumerViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = ConsumerSerializer
    queryset = Consumer.objects.all()


class CompanyViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ComplainViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()
