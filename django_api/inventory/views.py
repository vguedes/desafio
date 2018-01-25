"""API Views"""

from rest_framework import viewsets
from rest_framework import (
    permissions,
    generics
)
from django_filters import rest_framework as filters
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
    filter_fields = ('name',)


class StateViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    filter_fields = ('name', 'country__name')


class CityViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_fields = ('name', 'state__name', 'state__country__name')


class ConsumerViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = ConsumerSerializer
    queryset = Consumer.objects.all()
    filter_fields = ('name', 'email')


class CompanyViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ComplainFilter(filters.FilterSet):
    created = filters.DateFilter()
    created_year = filters.NumberFilter(name='created', lookup_expr='year')
    created_month = filters.NumberFilter(name='created', lookup_expr='month')
    created_day = filters.NumberFilter(name='created', lookup_expr='day')
    created_min = filters.DateFilter(name='created', lookup_expr='gte')
    created_max = filters.DateFilter(name='created', lookup_expr='lte')

    class Meta:
        model = Complain
        fields = [
            'consumer',
            'city',
            'company',
            'created',
            'created_year',
            'created_month',
            'created_day',
            'created_min',
            'created_max',
            'title',
            'description'
        ]



class ComplainViewSet(IsAuthenticated, viewsets.ModelViewSet):
    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()
    filter_class = ComplainFilter


class CustomComplainListViewByCreatedRange(IsAuthenticated, generics.ListAPIView):
    serializer_class = ComplainSerializer

    def get_queryset(self):
        created_min = self.kwargs['created_min']
        created_max = self.kwargs['created_max']
        return Complain.objects.filter(
            created__gte=created_min,
            created__lte=created_max,
        )
