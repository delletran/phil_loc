import json
import logging

from alive_progress import alive_bar
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from importlib import resources

from ...models import Barangay, Municipality, Province, Region

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

data_src = 'phil_loc.static.data'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""

    logging.info("Delete Location instances".center(40, '-'))
    Barangay.objects.all().delete()
    Municipality.objects.all().delete()
    Province.objects.all().delete()
    Region.objects.all().delete()


def generate_regions():
    print("GENERATING REGIONS...")
    with resources.open_text(data_src, 'refregion.json') as refregion_file:
        dictionary_list = json.load(refregion_file)['RECORDS']

        total_regions = len(dictionary_list)
        print(f"total_regions :: {total_regions}")

        with alive_bar(total_regions, title="Generating PH REGIONS", title_length=50) as bar:
            for item in dictionary_list:
                id = item["id"]
                name = item["regDesc"]
                regCode = item["regCode"]
                bar.title("Creating Object for {}..".format(name))
                try:
                    if (Region.objects.filter(id=id).count() >= 1):
                        print(f"{name} already exist..")
                    else:
                        Region.objects.create(
                            id=item['id'],
                            name=item['regDesc'],
                            psgc_code=item['psgcCode'],
                            reg_code=regCode,
                            country='PH',
                        )

                except IntegrityError as e:
                    if str(e.__cause__) == "UNIQUE constraint failed: Region.regCode":
                        print("Object: {}..Skipped".format(name))
                    else:
                        print("Object: {}..{}".format(
                            name), e.__cause__)

                bar()


def generate_provinces():
    print("GENERATING Provinces...")
    with resources.open_text(data_src, 'refprovince.json') as refprovince_file:
        dictionary_list = json.load(refprovince_file)['RECORDS']

        total_provinces = len(dictionary_list)
        print(f"total_provinces :: {total_provinces}")

        with alive_bar(total_provinces, title="Generating PH Provinces", title_length=50) as bar:
            for item in dictionary_list:
                id = item["id"]
                name = item["provDesc"]
                reg_code = item["regCode"]
                prov_code = item["provCode"]
                bar.title("Creating Object for {}..".format(name))
                try:
                    if (Province.objects.filter(id=id).count() >= 1):
                        print(f"{name} already exist..")
                    else:
                        region = Region.objects.get(reg_code=reg_code)
                        Province.objects.create(
                            id=id,
                            name=name,
                            psgc_code=item['psgcCode'],
                            prov_code=prov_code,
                            reg_code=reg_code,
                            region=region
                        )

                except IntegrityError as e:
                    if str(e.__cause__) == "UNIQUE constraint failed: Province.prov_code":
                        print("Object: {}..Skipped".format(name))
                    else:
                        print("Object: {}..{}".format(
                            name), e.__cause__)

                bar()


def generate_municipality_cities():
    print("GENERATING municipality_city...")
    with resources.open_text(data_src, 'refcitymun.json') as refmunicipality_city_file:
        dictionary_list = json.load(refmunicipality_city_file)['RECORDS']

        total_municipality_city = len(dictionary_list)
        print(f"total_municipality_citys :: {total_municipality_city}")

        with alive_bar(total_municipality_city, title="Generating PH municipality_citys", title_length=50) as bar:
            for item in dictionary_list:

                id = item["id"]
                name = item["citymunDesc"]
                city_mun_code = item["citymunCode"]
                prov_code = item["provCode"]
                reg_code = item["regCode"]
                bar.title("Creating Object for {}..".format(name))
                try:
                    if (Municipality.objects.filter(id=id).count() >= 1):
                        print(f"{name} already exist..")
                    else:
                        province = Province.objects.filter(
                            prov_code=prov_code).first()
                        Municipality.objects.create(
                            id=id,
                            name=name,
                            psgc_code=item['psgcCode'],
                            city_mun_code=city_mun_code,
                            prov_code=prov_code,
                            reg_code=reg_code,
                            province=province
                        )

                except IntegrityError as e:
                    if str(e.__cause__) == "UNIQUE constraint failed: Municipality.city_mun_code":
                        print("Object: {}..Skipped".format(name))
                    else:
                        print("Object: {}..{}".format(
                            name), e.__cause__)

                bar()


def generate_barangays():
    print("GENERATING barangay...")
    with resources.open_text(data_src, 'refbrgy.json') as refbarangay_file:
        dictionary_list = json.load(refbarangay_file)['RECORDS']

        total_barangay = len(dictionary_list)
        print(f"total_barangays :: {total_barangay}")

        with alive_bar(total_barangay, title="Generating PH barangays", title_length=50) as bar:
            for item in dictionary_list:

                id = item["id"]
                name = item["brgyDesc"]
                brgy_code = item["brgyCode"]
                city_mun_code = item["citymunCode"]
                prov_code = item["provCode"]
                reg_code = item["regCode"]
                bar.title("Creating Object for {}..".format(name))
                try:
                    if (Barangay.objects.filter(id=id).count() >= 1):
                        print(f"{name} already exist..")
                    else:
                        municipality = Municipality.objects.filter(
                            city_mun_code=city_mun_code).first()
                        Barangay.objects.create(
                            id=id,
                            name=name,
                            brgy_code=brgy_code,
                            city_mun_code=city_mun_code,
                            prov_code=prov_code,
                            reg_code=reg_code,
                            municipality=municipality
                        )

                except IntegrityError as e:
                    if str(e.__cause__) == "UNIQUE constraint failed: Barangay.brgy_code":
                        print("Object: {}..Skipped".format(name))
                    else:
                        print("Object: {}..{}".format(
                            name), e.__cause__)

                bar()


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    if mode == MODE_REFRESH:
        clear_data()

    if mode == MODE_CLEAR:
        clear_data()
        return
    generate_regions()
    generate_provinces()
    generate_municipality_cities()
    generate_barangays()
