import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, **options):
        print(os.environ.get("ADMIN_USERNAME"))
        User = get_user_model()
        try:
            User.objects.create_superuser(
                os.environ.get("ADMIN_USERNAME"),
                os.environ.get("ADMIN_EMAIL"),
                os.environ.get("ADMIN_PASSWORD")
                )
        except IntegrityError:
            pass
