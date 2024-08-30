from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Barangay(models.Model):
    class Meta:
        db_table = 'db_barangay'
        ordering = ['-pk']
        verbose_name = "Barangay"
        verbose_name_plural = "Barangays"

    name = models.CharField(max_length=64)
    brgy_code = models.IntegerField(blank=True, null=True)
    city_mun_code = models.IntegerField(blank=True, null=True)
    prov_code = models.IntegerField(blank=True, null=True)
    reg_code = models.IntegerField(blank=True, null=True)
    municipality = models.ForeignKey(
        "Municipality",
        verbose_name=_("Municipality"),
        db_column='municipality_id',
        related_name='barangay_municipality',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.pk} | {self.brgy_code} - {self.name}"


class Municipality(models.Model):
    class Meta:
        db_table = 'db_municipality'
        ordering = ['-pk']
        verbose_name = "Municipality"
        verbose_name_plural = "Municipalities"

    name = models.CharField(max_length=64)
    psgc_code = models.IntegerField(blank=True, null=True)
    city_mun_code = models.IntegerField(blank=True, null=True)
    prov_code = models.IntegerField(blank=True, null=True)
    reg_code = models.IntegerField(blank=True, null=True)
    province = models.ForeignKey(
        "Province",
        verbose_name=_("Province"),
        db_column='province_id',
        related_name='municipality_province',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.pk} | {self.city_mun_code} - {self.name}"


class Province(models.Model):
    class Meta:
        db_table = 'db_province'
        ordering = ['-pk']
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    name = models.CharField(max_length=64)
    psgc_code = models.IntegerField(blank=True, null=True)
    prov_code = models.IntegerField(blank=True, null=True)
    reg_code = models.IntegerField(blank=True, null=True)
    region = models.ForeignKey(
        "Region",
        verbose_name=_("Region"),
        db_column='region_id',
        related_name='province_region',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.pk} | {self.prov_code} - {self.name}"


class COUNTRY(models.TextChoices):
    PH = 'PH', 'Philippines'


class Region(models.Model):
    class Meta:
        db_table = 'db_region'
        ordering = ['-pk']
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    name = models.CharField(max_length=64)
    psgc_code = models.IntegerField(blank=True, null=True)
    reg_code = models.IntegerField(unique=True)
    country = models.CharField(
        "Country",
        max_length=4,
        choices=COUNTRY.choices,
        default=COUNTRY.PH,
    )

    def __str__(self) -> str:
        return f"{self.pk} | {self.reg_code} - {self.name}"


class PhAddress(models.Model):
    class Meta:
        db_table = 'db_ph_address'
        ordering = ['-pk']
        verbose_name = "Phillipines Address"
        verbose_name_plural = "Phillipines Addresses"

    country = models.CharField(
        "Country",
        max_length=4,
        choices=COUNTRY.choices,
        default=COUNTRY.PH,
    )
    region = models.ForeignKey(
        to=Region,
        verbose_name=_("Region"),
        db_column='region_id',
        related_name='address_region',
        on_delete=models.DO_NOTHING,
    )
    province = models.ForeignKey(
        to=Province,
        verbose_name=_("Province"),
        db_column='province_id',
        related_name='address_province',
        on_delete=models.DO_NOTHING,
    )
    municipality = models.ForeignKey(
        to=Municipality,
        verbose_name=_("Municipality"),
        db_column='municipality_id',
        related_name='ph_addresses',
        on_delete=models.DO_NOTHING,
    )
    barangay_district = models.ForeignKey(
        to=Barangay,
        verbose_name=_("Barangay"),
        db_column='barangay_id',
        related_name='address_barangay',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    unit_home_street = models.CharField(
        max_length=256, null=True, default=None)
    zip_code = models.IntegerField(blank=True, null=True, default=None)
    district_id = models.IntegerField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.pk}"
