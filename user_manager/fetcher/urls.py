from django.urls import path

from . import views

urlpatterns = [
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
        views.get_all_manufacturer_list,
        name="manufacturer_list",
    ),
    path(
        "car-list/",
        views.get_all_car_list,
        name="car_list",
    ),
]
