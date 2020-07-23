from django.db import models
from django.conf import settings
from modules.person.models import Persons


class Movies(models.Model):
    tittle = models.CharField(max_length=50)
    release_year = models.CharField(max_length=5)
    casting = models.ManyToManyField(Persons, null=True)
    directors = models.ManyToManyField(Persons, null=True)
    producers = models.ManyToManyField(Persons, null=True)
    pro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.tittle} {self.release_year}"
