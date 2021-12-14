from django.db import models

# Create your models here.
from django.db.models import IntegerField, CharField


class TestModeltest(models):
    name = CharField(max_length=200, null=True, blank=True)
    number = IntegerField(default=0, null=True, blank=True)


