from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Manufacturer, Car
from rest_framework import status, generics
from transport.constants import constant

from django.shortcuts import render
from .models import Users
from .serializers import (
    UserSerializer,
    ManufacturerSerializer,
    CarSerializer,
    AuthCustomTokenSerializer,
    ManufacturerListGetSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.core import exceptions


@api_view(["POST"])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid(raise_exception=True):
        validated_data = serialized.validated_data
        user = Users.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.is_staff = True
        group_obj = Group.objects.get(name="View_Manufacture_and_car")
        user.groups.add(group_obj)
        user.save()
        return Response(
            {"Success": "User created Successfully"}, status=status.HTTP_201_CREATED
        )


class ObtainAuthToken(APIView):
    authentication_classes = ()
    throttle_classes = ()
    permission_classes = ()

    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        content = {
            "token": token.key,
        }

        return Response(content)


class ManufacturerViews(APIView):
    """
    ManufacturerViews is used to create, update, fetch and delete objects
    """

    permission_classes = [permissions.IsAdminUser]

    @classmethod
    def post(self, request, format=None):
        """
        This causes a Manufacturer to be created
        :param request:
        :return: Manufacturer data and status 201 created
        """
        serializer = ManufacturerSerializer(data=request.data)

        # check serializer validation
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serial_data = serializer.data
            return Response(
                serial_data,
                status=status.HTTP_201_CREATED,
            )

    @classmethod
    def get(cls, request, manufacturer_id):
        """
        returns specified Manufacturer
        :param request:
        :param manufacturer_id
        :return: returns specified manufacturer object
        """
        try:

            manufacturer_obj = Manufacturer.objects.get(id=manufacturer_id)
            serializer = ManufacturerListGetSerializer(manufacturer_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Manufacturer.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant["InvalidManufacturerId"].format(
                        manufacturer_id
                    )
                },
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def patch(cls, request, manufacturer_id):
        """
        This updates the specified manufacturer
        :param request:
        :param manufacturer_id:
        :return: Updated object response with status 200 OK
        """
        try:
            manufacturer_obj = Manufacturer.objects.get(id=manufacturer_id)
            serializer = ManufacturerSerializer(
                manufacturer_obj, data=request.data, partial=True
            )

            # check serializer validation
            if serializer.is_valid(raise_exception=True):
                serial_data = serializer.validated_data
                serializer.save()
                manufacturer_obj = Manufacturer.objects.get(id=manufacturer_id)
                serializer = ManufacturerSerializer(manufacturer_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Manufacturer.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant["InvalidManufacturerId"].format(
                        manufacturer_id
                    )
                },
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def delete(cls, request, manufacturer_id):
        """
        This deletes the specified Manufacturer
        :param request:
        :param manufacturer_id:
        :return: empty response with status 200 OK
        """
        try:
            manufacturer_obj = Manufacturer.objects.get(id=manufacturer_id)
            manufacturer_obj.delete()
            return Response({}, status=status.HTTP_200_OK)
        except ServicePlanConfiguration.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant["InvalidManufacturerId"].format(
                        manufacturer_id
                    )
                },
                status.HTTP_404_NOT_FOUND,
            )


class CarViews(APIView):
    """
    CarViews is used to create, update, fetch and delete objects
    """

    permission_classes = [permissions.IsAdminUser]

    @classmethod
    def post(self, request, format=None):
        """
        This causes a car to be created
        :param request:
        :return: car data and status 201 created
        """
        serializer = CarSerializer(data=request.data)
        # check serializer validation
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serial_data = serializer.data
            return Response(
                serial_data,
                status=status.HTTP_201_CREATED,
            )

    @classmethod
    def get(cls, request, car_id):
        """
        returns specified car
        :param request:
        :param car_id
        :return: returns specified manufacturer object
        """
        try:

            car_obj = Car.objects.get(id=car_id)
            serializer = CarSerializer(car_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {constant["Error"]: constant["InvalidCarId"].format(car_id)},
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def patch(cls, request, car_id):
        """
        This updates the specified car
        :param request:
        :param car_id:
        :return: Updated object response with status 200 OK
        """
        try:
            car_obj = Car.objects.get(id=car_id)
            serializer = CarSerializer(car_obj, data=request.data, partial=True)

            # check serializer validation
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                car_obj = Car.objects.get(id=car_id)
                serializer = CarSerializer(car_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {constant["Error"]: constant["InvalidCarId"].format(car_id)},
                status.HTTP_404_NOT_FOUND,
            )

    @classmethod
    def delete(cls, request, car_id):
        """
        This deletes the specified car
        :param car_id:
        :return: empty response with status 200 OK
        """
        try:
            car_obj = Car.objects.get(id=car_id)
            car_obj.delete()
            return Response({}, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {constant["Error"]: constant["InvalidCarId"].format(car_id)},
                status.HTTP_404_NOT_FOUND,
            )


class ManufacturerListViews(generics.ListAPIView):
    """
    GET: List Manufacturer
    """

    serializer_class = ManufacturerListGetSerializer

    def get_queryset(self):
        """
        It will return the list Manufacturer objects
        """
        return Manufacturer.objects.all()


class CarListViews(generics.ListAPIView):
    """
    GET: List Cars
    """

    serializer_class = CarSerializer

    def get_queryset(self):
        """
        It will return the list Car objects
        """
        return Car.objects.all()
