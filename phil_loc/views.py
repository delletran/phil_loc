from rest_framework.generics import ListAPIView

from .models import Barangay, Municipality, Province, Region
from .serializers import (BarangaySerializer, CityMunSerializer,
                           ProvinceSerializer, RegionSerializer)


class RegionListAPIView(ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class ProvinceListAPIView(ListAPIView):
    serializer_class = ProvinceSerializer

    def get_queryset(self):
        reg_code = self.kwargs.get('reg_code')
        if reg_code is not None:
            return Province.objects.filter(reg_code=reg_code)
        else:
            return Province.objects.all()


class CityMunListAPIView(ListAPIView):
    serializer_class = CityMunSerializer

    def get_queryset(self):
        prov_code = self.kwargs.get('prov_code')
        if prov_code is not None:
            return Municipality.objects.filter(prov_code=prov_code)
        else:
            return Municipality.objects.all()


class BarangayListAPIView(ListAPIView):
    serializer_class = BarangaySerializer

    def get_queryset(self):
        city_mun_code = self.kwargs.get('city_mun_code')
        if city_mun_code is not None:
            return Barangay.objects.filter(city_mun_code=city_mun_code)
        else:
            return Barangay.objects.all()
