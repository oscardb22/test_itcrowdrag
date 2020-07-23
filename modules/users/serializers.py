from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import Users
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class CreateUserSerializable(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'email', 'date_joined', 'last_login', 'is_active']
        read_only_fields = ['id', 'date_joined', 'last_login', 'is_active']

    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        if 'email' in validated_data:
            instance.email = validated_data['email']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("CellPhone, Email or Username"),
        trim_whitespace=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')

            if not user.is_active:
                msg = _('User is not active.')
                raise serializers.ValidationError(msg, code='User is not active')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        user.last_login = datetime.now()
        user.save()
        list_token = Token.objects.filter(user=user)
        if list_token.exists():
            list_token.delete()
        token = Token.objects.create(user=user)
        attrs['token'] = token
        return attrs
