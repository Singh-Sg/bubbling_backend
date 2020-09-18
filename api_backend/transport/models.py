import uuid

from django.db import models


def uuid_str():
    return str(uuid.uuid4())

UNITED_STATES = 1
RUSSIA = 2
CHINA = 3
GERMANY = 4
UNITED_KINGDOM = 5
FRANCE = 6
JAPAN = 7
ISRAEL = 8
INDIA = 9
CANADA = 10

COUNTRY_CHOICES = (
    (UNITED_STATES, 'United States'),
    (RUSSIA, 'Russia'),
    (CHINA, 'China'),
    (GERMANY, 'Germany'),
    (UNITED_KINGDOM, 'United Kingdom'),
    (FRANCE, 'France'),
    (JAPAN, 'Japan'),
    (ISRAEL, 'Israel'),
    (INDIA, 'India'),
    (CANADA, 'Canada')
)


class Manufacturer(models.Model):
    class Meta:
        db_table = "manufacturers"

    id = models.CharField(primary_key=True, default=uuid_str, max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    country = models.IntegerField(choices=COUNTRY_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)


class Car(models.Model):
    class Meta:
        db_table = "cars"

    id = models.CharField(primary_key=True, default=uuid_str, max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    number_of_doors = models.IntegerField()
    price = models.FloatField()
    model_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

