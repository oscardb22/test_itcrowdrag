from rest_framework import serializers
from .models import Movies
from modules.person.serializers import CreatePersonsSerializable
from modules.funtions import int_to_roman


class CreateMoviesSerializable(serializers.ModelSerializer):
    release_year = serializers.IntegerField(min_value=1888, initial=4000)

    class Meta:
        model = Movies
        fields = ['id', 'tittle', 'release_year', 'casting', 'directors', 'producers']
        read_only_fields = ['id', ]


class ListMoviesSerializable(serializers.ModelSerializer):
    casting = CreatePersonsSerializable(many=True, read_only=True)
    directors = CreatePersonsSerializable(many=True, read_only=True)
    producers = CreatePersonsSerializable(many=True, read_only=True)
    release_year = serializers.SerializerMethodField(method_name='get_release_year')

    @staticmethod
    def get_release_year(obj):
        return int_to_roman(obj.release_year)

    class Meta:
        model = Movies
        fields = ['id', 'tittle', 'release_year', 'casting', 'directors', 'producers']
        read_only_fields = ['id', ]
