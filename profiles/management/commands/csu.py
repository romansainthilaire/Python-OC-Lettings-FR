from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("username")
        parser.add_argument("password")

    def handle(self, **options):
        User = get_user_model()
        try:
            User.objects.create_superuser(
                username=options["username"],
                password=options["password"]
                )
        except IntegrityError:
            pass
