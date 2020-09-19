from django.shortcuts import render
from .models import Users
from .serializers import UserSerializer, AuthCustomTokenSerializer, UserInfoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
import requests
import json
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token

api_backend_base_url = "http://127.0.0.1:8001"


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid(raise_exception=True):
        validated_data = serialized.validated_data
        resp = requests.post(
            api_backend_base_url + "/users/create_auth/",
            data=request.data,
            headers={"Authorization": "Token " + request.user.api_backend_token},
        )
        if resp.status_code == 201:
            user = Users.objects.create(
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
            )
            user.set_password(validated_data["password"])
            user.save()
            serial_data = serialized.data
            info = UserInfoSerializer(user)
            return Response({"data": info.data}, status=status.HTTP_201_CREATED)
        return Response(
            {"Error": json.loads(resp.content)}, status=status.HTTP_400_BAD_REQUEST
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
        resp = requests.post(
            api_backend_base_url + "/users/token-auth/",
            data=request.data,
        )
        if resp.status_code == 200:
            user = serializer.validated_data["user"]
            user.api_backend_token = json.loads(resp.content)["token"]
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            content = {
                "token": token.key,
            }
            return Response(content)
        return Response({"Error": "Issue with backend services"})


@api_view(["GET"])
def get_profile(request):
    """
    Get login user info
    """
    user = UserInfoSerializer(request.user)
    return Response({"data": user.data}, status=status.HTTP_201_CREATED)
