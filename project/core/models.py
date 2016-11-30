from __future__ import unicode_literals

from django.db import models


class Path(models.Model):
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")

    def __str__(self):
        return self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "pois": [poi.json() for poi in self.poi_set.all()]
        }


class POI(models.Model):
    name = models.CharField("Name", max_length=255)
    latitude = models.FloatField("Latitude")
    longitude = models.FloatField("Longitude")
    path = models.ForeignKey(Path)

    def __str__(self):
        return self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
