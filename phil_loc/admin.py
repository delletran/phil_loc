from django.apps import apps
from django.contrib import admin

admin.site.register(apps.all_models['phil_loc'].values())
