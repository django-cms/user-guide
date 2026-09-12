#!/usr/bin/env python3
"""Seed a freshly generated django CMS project for screenshot capture."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

PAGE_REVERSE_ID = "user-guide-screenshot-home"


def seed_site(
    project_dir: Path,
    *,
    username: str,
    password: str,
    email: str,
) -> str:
    project_dir = project_dir.resolve()
    if not (project_dir / "manage.py").is_file():
        raise RuntimeError(f"No django CMS project found in {project_dir}")

    sys.path.insert(0, str(project_dir))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "screenshot_site.settings")

    import django

    django.setup()

    from cms.api import add_plugin, create_page
    from cms.models import Page
    from django.contrib.auth import get_user_model
    from django.contrib.sites.models import Site

    user_model = get_user_model()
    user, _ = user_model.objects.update_or_create(
        username=username,
        defaults={
            "email": email,
            "is_active": True,
            "is_staff": True,
            "is_superuser": True,
        },
    )
    user.set_password(password)
    user.save(update_fields=["password"])

    site = Site.objects.get_current()
    site.domain = "127.0.0.1"
    site.name = "django CMS"
    site.save(update_fields=["domain", "name"])

    page = Page.objects.filter(reverse_id=PAGE_REVERSE_ID).first()
    if page is None:
        page = create_page(
            title="Welcome",
            template="base.html",
            language="en",
            slug="welcome",
            reverse_id=PAGE_REVERSE_ID,
            in_navigation=True,
            created_by=user,
            site=site,
        )

    placeholder = page.get_placeholders("en").get(slot="Page Content")
    if not placeholder.get_plugins("en").exists():
        container = add_plugin(
            placeholder,
            "GridContainerPlugin",
            "en",
            config={
                "container_type": "container",
                "plugin_title": {"title": "Main content"},
            },
        )
        add_plugin(
            placeholder,
            "TextPlugin",
            "en",
            target=container,
            body=(
                "<h1>Welcome to the django CMS user guide</h1>"
                "<p>This page provides stable content for automated screenshots.</p>"
            ),
        )

    return page.get_absolute_url(language="en")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--username", default="admin")
    parser.add_argument("--password", required=True)
    parser.add_argument("--email", default="admin@example.com")
    return parser


def main() -> int:
    arguments = build_parser().parse_args()
    try:
        page_url = seed_site(
            arguments.project_dir,
            username=arguments.username,
            password=arguments.password,
            email=arguments.email,
        )
    except Exception as error:  # noqa: BLE001 - present fixture failures concisely.
        print(f"error: could not seed screenshot site: {error}", file=sys.stderr)
        return 1
    print(f"PAGE_URL={page_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
