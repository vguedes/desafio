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
from rest_framework import permissions
from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class ConsumerViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumerSerializer
    queryset = Consumer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class ComplainFilter(filters.FilterSet):
    min_date = filters.DateFromToRangeFilter(name='datetime', lookup_expr='gte')
    max_date = filters.DateFromToRangeFilter(name='datetime', lookup_expr='lte')

    class Meta:
        model = Complain
        fields = [
            'consumer',
            'city',
            'company',
            'min_date',
            'max_date',
            'title',
            'description'
        ]



class ComplainViewSet(viewsets.ModelViewSet):
    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DateFromToRangeFilter,)
    filter_class = ComplainFilter
