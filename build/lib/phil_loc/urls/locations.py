from django.urls import path

from ..views.locations import (BarangayListAPIView, CityMunListAPIView,
                               ProvinceListAPIView, RegionListAPIView)

app_name = 'locations'

urlpatterns = [
    path('regions/',
         RegionListAPIView.as_view(), name='region-list'),
    path('regions/<int:reg_code>/provinces/',
         ProvinceListAPIView.as_view(), name='province-list'),
    path('provinces/<int:prov_code>/municipalities/',
         CityMunListAPIView.as_view(), name='municipality-list'),
    path('municipalities/<int:city_mun_code>/barangays/',
         BarangayListAPIView.as_view(), name='barangays-list'),
]
