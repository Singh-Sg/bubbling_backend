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
]