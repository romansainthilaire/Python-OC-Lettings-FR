import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("username", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("password", type=str)

    def handle(self, **options):
        print("This is the admin username : " + os.getenv("ADMIN_USERNAME"))
        User = get_user_model()
        try:
            User.objects.create_superuser(
                username=options["username"],
                email=options["email"],
                password=options["password"],
                )
        except IntegrityError:
            pass
