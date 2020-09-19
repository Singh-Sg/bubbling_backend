from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.core import exceptions

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = UserModel
        fields = ('password', 'email', 'first_name', 'last_name',)


class UserInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    user_uuid = serializers.CharField()

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name','user_uuid',)


class AuthCustomTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if validate_email(email):
                user_request = get_object_or_404(
                    User,
                    email=email,
                )

                email = user_request.username

            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password"')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs