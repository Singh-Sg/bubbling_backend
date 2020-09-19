from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import requests
from rest_framework import status, generics
from django.http import Http404, JsonResponse, StreamingHttpResponse
import json
from .constants import constant
from rest_framework.decorators import api_view

api_backend_base_url = "http://127.0.0.1:8001"


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
        try:
            resp = requests.post(
                api_backend_base_url + "/manufacturer/",
                data=request.data,
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
                status.HTTP_404_NOT_FOUND,
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
            resp = requests.get(
                api_backend_base_url + "/manufacturer/" + manufacturer_id + "/",
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
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
            resp = requests.patch(
                api_backend_base_url + "/manufacturer/" + manufacturer_id + "/",
                data=request.data,
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
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
            resp = requests.delete(
                api_backend_base_url + "/manufacturer/" + manufacturer_id + "/",
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
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
        try:
            if request.data.get("owner") == request.user.user_uuid:
                return Response(
                    {constant["Error"]: constant["AdminOwnerIssue"]},
                    status.HTTP_400_BAD_REQUEST,
                )

            resp = requests.post(
                api_backend_base_url + "/car/",
                data=request.data,
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
                status.HTTP_404_NOT_FOUND,
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
            resp = requests.get(
                api_backend_base_url + "/car/" + car_id + "/",
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
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
            resp = requests.patch(
                api_backend_base_url + "/car/" + car_id + "/",
                data=request.data,
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
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
            resp = requests.delete(
                api_backend_base_url + "/car/" + car_id + "/",
                headers={"Authorization": "Token " + request.user.api_backend_token},
            )
            return JsonResponse(json.loads(resp.content), status=resp.status_code)
        except Exception as e:
            return Response(
                {constant["Error"]: constant["ApiBackendError"]},
                status.HTTP_404_NOT_FOUND,
            )


@api_view(["GET"])
def get_all_manufacturer_list(request):
    """
    Get manufacturer data
    """
    resp = requests.get(
        api_backend_base_url + "/manufacturer-list/",
        headers={"Authorization": "Token " + request.user.api_backend_token},
    )
    return JsonResponse(
        {"manufacturer_data": json.loads(resp.content)}, status=resp.status_code
    )


@api_view(["GET"])
def get_all_car_list(request):
    """
    Get car data
    """
    resp = requests.get(
        api_backend_base_url + "/car-list/",
        headers={"Authorization": "Token " + request.user.api_backend_token},
    )
    return JsonResponse({"car_data": json.loads(resp.content)}, status=resp.status_code)
