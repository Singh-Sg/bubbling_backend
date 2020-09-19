from django.urls import path

from . import views

urlpatterns = [
    #  SignUp api
    path(
        "create_auth/",
        views.create_auth,
        name="create_auth",
    ),
    path(
        "token-auth/",
        views.ObtainAuthToken.as_view(),
        name="auth_token",
    ),
]
