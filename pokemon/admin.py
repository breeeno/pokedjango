from django.contrib import admin
from pokemon.models import Pokemon
from rest_framework.authtoken.admin import TokenAdmin
admin.site.register(Pokemon)

TokenAdmin.raw_id_fields = ['user']
