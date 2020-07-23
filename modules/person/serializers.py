from rest_framework import serializers
from .models import Persons


class CreatePersonsSerializable(serializers.ModelSerializer):

    class Meta:
        model = Persons
        fields = ['id', 'first_name', 'last_name', 'aliases']
        read_only_fields = ['id', ]

