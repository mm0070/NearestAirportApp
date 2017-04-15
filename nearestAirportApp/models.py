# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Airportslist(models.Model):
    icao = models.TextField(db_column='ICAO', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='LON', blank=True, null=True)  # Field name made lowercase.
    elevation = models.IntegerField(db_column='Elevation', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.icao

    class Meta:
        managed = False
        db_table = 'airportsList'

