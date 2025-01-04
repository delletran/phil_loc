from rest_framework import serializers

from .models import (PhAddress, Barangay, Municipality, Province, Region)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "reg_code"]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ["id", "name", "prov_code"]


class CityMunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ["id", "name", "city_mun_code"]


class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = ["id", "name", "brgy_code"]


class RegionSerializerRepresentation(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name"]

    def to_representation(self, instance):
        return instance.name


class ProvinceSerializerRepresentation(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ["id", "name"]

    def to_representation(self, instance):
        return instance.name


class CityMunSerializerRepresentation(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ["id", "name"]

    def to_representation(self, instance):
        return instance.name


class BarangaySerializerRepresentation(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = ["id", "name"]

    def to_representation(self, instance):
        return instance.name


class PhAddressUpsertSerializer(serializers.ModelSerializer):
    region_id = serializers.PrimaryKeyRelatedField(
        queryset=Region.objects.all(),
        source='region',
        required=True
    )
    province_id = serializers.PrimaryKeyRelatedField(
        queryset=Province.objects.all(),
        source='province',
        required=True
    )
    municipality_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipality.objects.all(),
        source='municipality',
        required=True
    )
    barangay_district_id = serializers.PrimaryKeyRelatedField(
        queryset=Barangay.objects.all(),
        source='barangay_district',
        required=True
    )

    class Meta:
        model = PhAddress
        fields = [
            'id',
            'country',
            'region_id',
            'province_id',
            'municipality_id',
            'barangay_district_id',
            'unit_home_street',
            'zip_code',
            'district_id',
            'updated_at'
        ]


class PhAddressSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    province = ProvinceSerializer()
    municipality = CityMunSerializer()
    barangay_district = BarangaySerializer()

    class Meta:
        model = PhAddress
        fields = [
            'id',
            'country',
            'region',
            'province',
            'municipality',
            'barangay_district',
            'unit_home_street',
            'zip_code',
            'district_id',
            'updated_at',
        ]
