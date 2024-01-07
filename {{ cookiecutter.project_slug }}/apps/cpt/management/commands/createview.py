"""
createview.py
Ian Kollipara <ian.kollipara@cune.edu>

Create a new Django View
"""

from django.core.management import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.conf import settings


class Command(BaseCommand):
    help = "Create a new Django View"

    def add_arguments(self, parser):
        parser.add_argument("view_name", type=str)
        parser.add_argument("--app-name", type=str, default="")

    def handle(self, *args, **options):
        view_name = options["view_name"]
        app_name = options["app_name"]
        if not view_name:
            raise CommandError("View name is required")

        (settings.BASE_DIR / "templates" / app_name / f"{view_name}.html").write_text((render_to_string("cpt/view.html.template")))

        self.stdout.write(self.style.SUCCESS(f"Successfully created view {app_name + "/"}{view_name}.html"))
