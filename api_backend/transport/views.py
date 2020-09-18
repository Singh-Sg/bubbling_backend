from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Manufacturer, Car
from .serializer import ManufacturerSerializer, CarSerializer
from rest_framework import status, generics
from transport.constants import constant


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
            serializer = ManufacturerSerializer(
                manufacturer_obj
            )
            return Response(serializer.data,  status=status.HTTP_200_OK)
        except Manufacturer.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant[
                        "InvalidManufacturerId"
                    ].format(manufacturer_id)
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
            serializer = ManufacturerSerializer(manufacturer_obj, data=request.data, partial=True)

            # check serializer validation
            if serializer.is_valid(raise_exception=True):
                serial_data = serializer.validated_data
                serializer.save()
                manufacturer_obj = Manufacturer.objects.get(id=manufacturer_id)
                serializer = ManufacturerSerializer(
                    manufacturer_obj
                )
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Manufacturer.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant[
                        "InvalidManufacturerId"
                    ].format(manufacturer_id)
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
            manufacturer_obj = Manufacturer.objects.get(id=manufacturer_id
            )
            manufacturer_obj.delete()
            return Response({}, status=status.HTTP_200_OK)
        except ServicePlanConfiguration.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant[
                        "InvalidManufacturerId"
                    ].format(manufacturer_id)
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
            serializer = CarSerializer(
                car_obj
            )
            return Response(serializer.data,  status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant[
                        "InvalidCarId"
                    ].format(car_id)
                },
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
                serializer = CarSerializer(
                    car_obj
                )
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant[
                        "InvalidCarId"
                    ].format(car_id)
                },
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
            car_obj = Car.objects.get(id=car_id
            )
            car_obj.delete()
            return Response({}, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response(
                {
                    constant["Error"]: constant[
                        "InvalidCarId"
                    ].format(car_id)
                },
                status.HTTP_404_NOT_FOUND,
            )


class ManufacturerListViews(generics.ListAPIView):
    """
    GET: List Manufacturer
    """

    serializer_class = ManufacturerSerializer

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