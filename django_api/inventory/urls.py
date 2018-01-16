from django.conf.urls import url, include
from rest_framework import routers
from inventory import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'consumers', views.ConsumerViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'complains', views.ComplainViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
]
