# from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from modules.person.models import Persons


class Movies(models.Model):
    tittle = models.CharField(max_length=50)
    release_year = models.IntegerField()
    """
    release_year = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex='^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',
                message='Roman number invalid',
                code='invalid_release_year'
            ),
        ]
    )
    """
    casting = models.ManyToManyField(Persons, related_name='movie_casting')
    directors = models.ManyToManyField(Persons, related_name='movie_directors')
    producers = models.ManyToManyField(Persons, related_name='movie_producers')
    pro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.tittle} {self.release_year}"
