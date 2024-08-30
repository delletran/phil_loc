from django.test import TestCase
from phil_loc.models import Barangay, Municipality, Province, Region, PhAddress


class RegionModelTest(TestCase):

    def setUp(self):
        self.region = Region.objects.create(
            name="Test Region",
            psgc_code=123456,
            reg_code=12
        )

    def test_region_creation(self):
        self.assertEqual(self.region.name, "Test Region")
        self.assertEqual(self.region.psgc_code, 123456)
        self.assertEqual(self.region.reg_code, 12)
        self.assertTrue(isinstance(self.region, Region))
        self.assertEqual(str(
            self.region), f"{self.region.pk} | {self.region.reg_code} - {self.region.name}")


class ProvinceModelTest(TestCase):

    def setUp(self):
        self.region = Region.objects.create(
            name="Test Region",
            psgc_code=123456,
            reg_code=12
        )
        self.province = Province.objects.create(
            name="Test Province",
            psgc_code=654321,
            prov_code=21,
            reg_code=12,
            region=self.region
        )

    def test_province_creation(self):
        self.assertEqual(self.province.name, "Test Province")
        self.assertEqual(self.province.psgc_code, 654321)
        self.assertEqual(self.province.prov_code, 21)
        self.assertEqual(self.province.region, self.region)
        self.assertTrue(isinstance(self.province, Province))
        self.assertEqual(str(
            self.province), f"{self.province.pk} | {self.province.prov_code} - {self.province.name}")


class MunicipalityModelTest(TestCase):

    def setUp(self):
        self.region = Region.objects.create(
            name="Test Region",
            psgc_code=123456,
            reg_code=12
        )
        self.province = Province.objects.create(
            name="Test Province",
            psgc_code=654321,
            prov_code=21,
            reg_code=12,
            region=self.region
        )
        self.municipality = Municipality.objects.create(
            name="Test Municipality",
            psgc_code=789012,
            city_mun_code=34,
            prov_code=21,
            reg_code=12,
            province=self.province
        )

    def test_municipality_creation(self):
        self.assertEqual(self.municipality.name, "Test Municipality")
        self.assertEqual(self.municipality.psgc_code, 789012)
        self.assertEqual(self.municipality.city_mun_code, 34)
        self.assertEqual(self.municipality.province, self.province)
        self.assertTrue(isinstance(self.municipality, Municipality))
        self.assertEqual(str(self.municipality),
                         f"{self.municipality.pk} | {self.municipality.city_mun_code} - {self.municipality.name}")


class BarangayModelTest(TestCase):

    def setUp(self):
        self.region = Region.objects.create(
            name="Test Region",
            psgc_code=123456,
            reg_code=12
        )
        self.province = Province.objects.create(
            name="Test Province",
            psgc_code=654321,
            prov_code=21,
            reg_code=12,
            region=self.region
        )
        self.municipality = Municipality.objects.create(
            name="Test Municipality",
            psgc_code=789012,
            city_mun_code=34,
            prov_code=21,
            reg_code=12,
            province=self.province
        )
        self.barangay = Barangay.objects.create(
            name="Test Barangay",
            brgy_code=987654,
            city_mun_code=34,
            prov_code=21,
            reg_code=12,
            municipality=self.municipality
        )

    def test_barangay_creation(self):
        self.assertEqual(self.barangay.name, "Test Barangay")
        self.assertEqual(self.barangay.brgy_code, 987654)
        self.assertEqual(self.barangay.municipality, self.municipality)
        self.assertTrue(isinstance(self.barangay, Barangay))
        self.assertEqual(str(
            self.barangay), f"{self.barangay.pk} | {self.barangay.brgy_code} - {self.barangay.name}")


class PhAddressModelTest(TestCase):

    def setUp(self):
        self.region = Region.objects.create(
            name="Test Region",
            psgc_code=123456,
            reg_code=12
        )
        self.province = Province.objects.create(
            name="Test Province",
            psgc_code=654321,
            prov_code=21,
            reg_code=12,
            region=self.region
        )
        self.municipality = Municipality.objects.create(
            name="Test Municipality",
            psgc_code=789012,
            city_mun_code=34,
            prov_code=21,
            reg_code=12,
            province=self.province
        )
        self.barangay = Barangay.objects.create(
            name="Test Barangay",
            brgy_code=987654,
            city_mun_code=34,
            prov_code=21,
            reg_code=12,
            municipality=self.municipality
        )
        self.ph_address = PhAddress.objects.create(
            region=self.region,
            province=self.province,
            municipality=self.municipality,
            barangay_district=self.barangay,
            unit_home_street="123 Main St",
            zip_code=1000,
        )

    def test_ph_address_creation(self):
        self.assertEqual(self.ph_address.region, self.region)
        self.assertEqual(self.ph_address.province, self.province)
        self.assertEqual(self.ph_address.municipality, self.municipality)
        self.assertEqual(self.ph_address.barangay_district, self.barangay)
        self.assertEqual(self.ph_address.unit_home_street, "123 Main St")
        self.assertEqual(self.ph_address.zip_code, 1000)
        self.assertTrue(isinstance(self.ph_address, PhAddress))
        self.assertEqual(str(self.ph_address), f"{self.ph_address.pk}")
