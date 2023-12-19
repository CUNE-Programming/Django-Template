"""
createapp.py
Ian Kollipara <ian.kollipara@cune.edu>
2023.12.18

Create Django App according to CPT
"""

from django.core.management import BaseCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string
from pathlib import Path
from os import getcwd, chdir

class Command(BaseCommand):
    help = "Create Django App according to CPT standards."

    def add_arguments(self, parser):
        parser.add_argument('name', required=True, help="Name of the app to generate")
        parser.add_argument(
            "--no-models",
            action='store_true',
            help="Do not generate models, migrations, and managers for this app",
            default=False
        )
        parser.add_argument(
            "--no-views",
            action='store_true',
            help="Do not generate views or urls for this app.",
            default=False
        )
        parser.add_argument("--dry-run", action='store_true', help="Do not actually generate any files", default=False)

    def handle(self, *args, **options):
        name = options["name"]
        no_models = options["no_models"]
        no_views = options["no_views"]
        dry_run = options["dry_run"]

        cwd = Path(getcwd())
        if not dry_run:
            Path(settings.BASE_DIR / "apps" / name).mkdir(parents=True, exist_ok=True)
            chdir(settings.BASE_DIR / "apps" / name)

        if not dry_run:
            Path("apps.py").write_text(
                render_to_string(
                    "cpt/apps.py.template",
                    {
                        "name": name,
                        "cls_name": "".join(map(str.capitalize, name.split("_")))
                    }
                )
            )

        if not dry_run:
            Path("__init__.py").touch()
        if not no_models:
            if not dry_run:
                Path("models.py").write_text(render_to_string("cpt/models.py.template"))
            if not dry_run:
                Path("managers.py").write_text(render_to_string("cpt/managers.py.template"))
            if not dry_run:
                Path("migrations").mkdir(exist_ok=True)
                Path("migrations/__init__.py").touch()
            if not dry_run:
                Path("admin.py").write_text(render_to_string("cpt/admin.py.template"))

        if not no_views:
            if not dry_run:
                Path("views.py").write_text(render_to_string("cpt/views.py.template"))
            if not dry_run:
                Path("urls.py").write_text(render_to_string("cpt/urls.py.template"))
            if not dry_run:
                Path("forms.py").write_text(render_to_string("cpt/forms.py.template"))
            if not dry_run:
                {% if cookiecutter.stack == 'THAD' %}
                Path(settings.BASE_DIR / "templates" / name).mkdir(exist_ok=True)
                {% endif %}{% if cookiecutter.stack == 'DIRT' %}
                Path(settings.BASE_DIR / "resources" / "pages" / name).mkdir(parents=True, exist_ok=True)
                {% endif %}

        if not dry_run:
            chdir(cwd)
        self.stdout.write(self.style.SUCCESS("Successfully created the app"))
        self.stdout.write(self.style.SUCCESS(f"Please add '{name}' to INSTALLED_APPS in settings.py"))
