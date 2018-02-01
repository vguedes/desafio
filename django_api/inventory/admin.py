from django.contrib import admin
from . import models

admin.site.register(models.Country)


# State Admin
class StateCountryListFilter(admin.SimpleListFilter):
    title = 'country'
    parameter_name = 'country'
    default_value = None

    def lookups(self, request, model_admin):
        countries = [
            (str(x.id), x.name) for
            x in
            models.Country.objects.all()
        ]
        return sorted(countries, key=lambda idx: idx[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(country_id=self.value())
        return queryset


class StateAdmin(admin.ModelAdmin):
    '''
        Admin View for State
    '''
    list_display = ('name', 'country')
    list_filter = (StateCountryListFilter,)
    search_fields = ('country__name', 'name')

admin.site.register(models.State, StateAdmin)


# CITY ADMIN
class StateListFilter(admin.SimpleListFilter):
    title = 'state'
    parameter_name = 'state'
    default_value = None

    def lookups(self, request, model_admin):
        states = [
            (str(x.id), x.name) for
            x in
            models.State.objects.all()
        ]
        return sorted(states, key=lambda idx: idx[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(state_id=self.value())
        return queryset


class CityCountryListFilter(admin.SimpleListFilter):
    title = 'country'
    parameter_name = 'country'
    default_value = None

    def lookups(self, request, model_admin):
        countries = [
            (str(x.id), x.name) for
            x in
            models.Country.objects.all()
        ]
        return sorted(countries, key=lambda idx: idx[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(state__country_id=self.value())
        return queryset


class CityAdmin(admin.ModelAdmin):
    '''
        Admin View for City
    '''

    def get_country_name(self, this_city):
        return this_city.state.country.name
    get_country_name.admin_order_field = 'state__country'
    get_country_name.short_description = 'country'

    def get_state_name(self, this_city):
        return this_city.state.name
    get_state_name.admin_order_field = 'state'
    get_state_name.short_description = 'state'

    list_display = ('name', 'get_state_name', 'get_country_name')
    list_filter = (CityCountryListFilter, StateListFilter)
    search_fields = ('state_name', 'state__country__name', 'name')

admin.site.register(models.City, CityAdmin)


# COMPANY ADMIN
class CompanyAdmin(admin.ModelAdmin):
    '''
        Admin View for Company
    '''
    list_display = ('name', 'city')
    list_filter = ('city',)
    search_fields = (
        'name',
        'city__name',
        'city__state__name',
        'city__state__country__name'
    )

admin.site.register(models.Company, CompanyAdmin)


# CONSUMER ADMIN
class EmailDomainsListFilter(admin.SimpleListFilter):
    title = 'e-mail domain'
    parameter_name = 'email'
    default_value = None

    def lookups(self, request, model_admin):
        domains = [
            (x.email.split('@')[1], x.email.split('@')[1]) for
            x in
            models.Consumer.objects.all()
        ]
        return sorted(domains, key=lambda idx: idx[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(email__endswith=self.value())
        return queryset


class ConsumerAdmin(admin.ModelAdmin):
    '''
        Admin View for Consumer
    '''
    list_display = ('name', 'email')
    list_filter = (EmailDomainsListFilter,)
    search_fields = ('name', 'email')

admin.site.register(models.Consumer, ConsumerAdmin)


# COMPLAIN ADMIN
class StateComplainListFilter(admin.SimpleListFilter):
    title = 'state (with complains)'
    parameter_name = 'state'
    default_value = None

    def lookups(self, request, model_admin):
        states = [
            (x.id, x.name) for
            x in
            models.State.objects.filter(
                city__complain__isnull=False
            )
        ]
        return sorted(states, key=lambda idx: idx[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(state__country_id=self.value())

class CityComplainListFilter(admin.SimpleListFilter):
    title = 'city (with complains)'
    parameter_name = 'city'
    default_value = None

    def lookups(self, request, model_admin):
        cities = [
            (x.id, x.name) for
            x in
            models.City.objects.filter(
                complain__isnull=False
            )
        ]
        return sorted(cities, key=lambda idx: idx[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(city__state__country_id=self.value())

class ComplainAdmin(admin.ModelAdmin):
    '''
        Admin View for Complain
    '''
    list_display = ('ellipsed_title', 'ellipsed_description', 'company', 'city')
    list_filter = (
        'company',
        'city__state__country',
        StateComplainListFilter,
        CityComplainListFilter,
    )
    search_fields = (
        'title',
        'description',
        'company__name',
        'consumer__name',
        'city__name',
        'city__state__name',
        'city__state__country__name'
    )

admin.site.register(models.Complain, ComplainAdmin)
