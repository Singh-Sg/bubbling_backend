from django.urls import path

from . import views

urlpatterns = [
    #  User signup api.
    path(
        "users/create_auth/",
        views.create_auth,
        name="create_auth",
    ),
    path('users/token-auth/', views.ObtainAuthToken.as_view(), name="auth_token",
    ),
    # This causes a manufacturer objects to be created and returns created manufacturer objects.
    path(
        "manufacturer/",
        views.ManufacturerViews.as_view(),
        name="manufacturer_create",
    ),
    # This returns, updates, deletes the specified Manufacturer objects
    path(
        "manufacturer/<str:manufacturer_id>/",
        views.ManufacturerViews.as_view(),
        name="manufacturer",
    ),
    # This causes a car objects to be created and returns created car objects.
    path(
        "car/",
        views.CarViews.as_view(),
        name="car_create",
    ),
    # This returns, updates, deletes the specified car objects
    path(
        "car/<str:car_id>/",
        views.CarViews.as_view(),
        name="car",
    ),
    path(
        "manufacturer-list/",
        views.ManufacturerListViews.as_view(),
        name="manufacturer_list",
    ),
    path(
        "car-list/",
        views.CarListViews.as_view(),
        name="car_list",
    ),
]