from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Displays current time"

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="View_Manufacture_and_car")
        if group:
            car_view = Permission.objects.get(codename="view_car")
            manu_view = Permission.objects.get(codename="view_manufacturer")
            group.permissions.add(car_view)
            group.permissions.add(manu_view)
            self.stdout.write(
                "Successfully Permission Added Into The View_Manufacture_and_car Group"
            )
