from django.core.management.base import BaseCommand
from Fins.models import Shop, Item, Department


class Command(BaseCommand):
    help = "Delete all data from database"

    def handle(self, *args, **kwargs):
        Item.objects.all().delete()
        Department.objects.all().delete()
        Shop.objects.all().delete()
        self.stdout.write("All data delete")
