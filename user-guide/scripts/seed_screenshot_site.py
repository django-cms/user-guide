#!/usr/bin/env python3
"""Seed a freshly generated django CMS project for screenshot capture."""

from __future__ import annotations

import argparse
import os
import sys
import warnings
from datetime import timedelta
from io import BytesIO
from pathlib import Path

PAGE_REVERSE_ID = "user-guide-screenshot-home"
LANGUAGE = "en"

PAGE_FIXTURES = (
    {
        "reverse_id": PAGE_REVERSE_ID,
        "title": "Welcome",
        "slug": "welcome",
        "in_navigation": True,
    },
    {
        "reverse_id": "user-guide-screenshot-about",
        "title": "About us",
        "slug": "about-us",
        "in_navigation": True,
        "published": True,
    },
    {
        "reverse_id": "user-guide-screenshot-services",
        "title": "Services",
        "slug": "services",
        "in_navigation": True,
        "published": True,
    },
    {
        "reverse_id": "user-guide-screenshot-consulting",
        "title": "Consulting",
        "slug": "consulting",
        "parent": "user-guide-screenshot-services",
        "in_navigation": True,
        "published": True,
    },
    {
        "reverse_id": "user-guide-screenshot-training",
        "title": "Training",
        "slug": "training",
        "parent": "user-guide-screenshot-services",
        "in_navigation": True,
    },
    {
        "reverse_id": "user-guide-screenshot-contact",
        "title": "Contact",
        "slug": "contact",
        "in_navigation": False,
    },
)


def _current_content(page, language: str = LANGUAGE):
    from cms.models import PageContent

    return PageContent.admin_manager.latest_content().get(
        page=page,
        language=language,
    )


def _content_placeholder(content):
    return content.get_placeholders().get(slot="Page Content")


def _page_versions(page, language: str = LANGUAGE):
    from djangocms_versioning.models import Version

    return [
        version
        for version in Version.objects.filter_by_grouper(page).order_by("pk")
        if version.content.language == language
    ]


def _version_in_state(page, state: str, language: str = LANGUAGE):
    return next(
        (version for version in _page_versions(page, language) if version.state == state),
        None,
    )


def _ensure_page(fixture, pages, site, user):
    from cms.api import create_page
    from cms.models import Page

    page = Page.objects.filter(reverse_id=fixture["reverse_id"]).first()
    if page is None:
        parent_id = fixture.get("parent")
        page = create_page(
            title=fixture["title"],
            template="base.html",
            language=LANGUAGE,
            slug=fixture["slug"],
            reverse_id=fixture["reverse_id"],
            parent=pages.get(parent_id),
            in_navigation=fixture.get("in_navigation", False),
            created_by=user,
            site=site,
        )
    return page


def _ensure_page_text(page, title: str) -> None:
    from cms.api import add_plugin

    placeholder = _content_placeholder(_current_content(page))
    if not placeholder.get_plugins(LANGUAGE).exists():
        add_plugin(
            placeholder,
            "TextPlugin",
            LANGUAGE,
            body=f"<h1>{title}</h1><p>Fixture content for the django CMS user guide.</p>",
        )


def _publish_draft(page, user, language: str = LANGUAGE) -> None:
    from djangocms_versioning.constants import DRAFT, PUBLISHED

    if _version_in_state(page, PUBLISHED, language) is None:
        draft = _version_in_state(page, DRAFT, language)
        if draft is not None:
            draft.publish(user)


def _ensure_filer_assets(user):
    from django.core.files.base import ContentFile
    from filer.models import File, Folder, Image
    from PIL import Image as PillowImage
    from PIL import ImageDraw

    folder, _ = Folder.objects.get_or_create(
        parent=None,
        name="Tutorial",
        defaults={"owner": user},
    )
    image = Image.objects.filter(
        folder=folder,
        original_filename="django-cms-tutorial.png",
    ).first()
    if image is None:
        canvas = PillowImage.new("RGB", (960, 540), "#f2f4f7")
        drawing = ImageDraw.Draw(canvas)
        drawing.rectangle((0, 0, 960, 110), fill="#243746")
        drawing.rectangle((80, 180, 880, 460), fill="#ffffff", outline="#d40055", width=8)
        drawing.rectangle((130, 235, 500, 275), fill="#d40055")
        drawing.rectangle((130, 315, 790, 340), fill="#a8b3bd")
        drawing.rectangle((130, 365, 690, 390), fill="#c5ccd3")
        data = BytesIO()
        canvas.save(data, format="PNG")
        image = Image.objects.create(
            folder=folder,
            owner=user,
            original_filename="django-cms-tutorial.png",
            name="django CMS tutorial image",
            default_alt_text="A sample django CMS page layout",
            default_caption="Tutorial fixture image",
            mime_type="image/png",
            file=ContentFile(data.getvalue(), name="django-cms-tutorial.png"),
        )

    document = File.objects.filter(
        folder=folder,
        original_filename="django-cms-user-guide.pdf",
    ).first()
    if document is None:
        document = File.objects.create(
            folder=folder,
            owner=user,
            original_filename="django-cms-user-guide.pdf",
            name="django CMS user guide",
            mime_type="application/pdf",
            file=ContentFile(
                b"%PDF-1.4\n% screenshot fixture document\n%%EOF\n",
                name="django-cms-user-guide.pdf",
            ),
        )
    return folder, image, document


def _ensure_alias(site, user):
    from cms.api import add_plugin
    from djangocms_alias.models import Alias, AliasContent, Category
    from djangocms_versioning.constants import DRAFT, PUBLISHED
    from djangocms_versioning.models import Version

    category = Category.objects.filter(translations__name="Shared sections").first()
    if category is None:
        category = Category.objects.create(name="Shared sections")
    alias, _ = Alias.objects.get_or_create(
        category=category,
        position=0,
        site=site,
    )
    draft = _version_in_alias_state(alias, DRAFT)
    published = _version_in_alias_state(alias, PUBLISHED)
    if draft is None and published is None:
        content = AliasContent.objects.with_user(user).create(
            alias=alias,
            name="Contact callout",
            language=LANGUAGE,
        )
        draft = Version.objects.get_for_content(content)
    editable_content = draft.content if draft is not None else published.content
    if not editable_content.placeholder.get_plugins(LANGUAGE).exists():
        add_plugin(
            editable_content.placeholder,
            "TextPlugin",
            LANGUAGE,
            body=(
                "<h2>Questions?</h2>"
                "<p>Contact the documentation team for help with django CMS.</p>"
            ),
        )
    if published is None:
        draft.publish(user)
        published = Version.objects.get(pk=draft.pk)
        draft = None
    if draft is None:
        # djangocms-alias creates the content copy before Version.copy attaches
        # its Version, which causes its patched manager to emit a false warning.
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="No user has been supplied when creating a new AliasContent",
                category=UserWarning,
            )
            published.copy(user)
    return alias


def _version_in_alias_state(alias, state: str):
    from djangocms_versioning.models import Version

    return next(
        (
            version
            for version in Version.objects.filter_by_grouper(alias).order_by("pk")
            if version.content.language == LANGUAGE and version.state == state
        ),
        None,
    )


def _frontend_image_config(image, existing=None):
    from djangocms_frontend.contrib.image.models import Image as FrontendImage

    config = FrontendImage(plugin_type="ImagePlugin").initialize_from_form().config
    config.update(existing or {})
    config.update(
        {
            "picture": {"pk": image.pk, "model": "filer.image"},
            "alignment": "center",
            "use_responsive_image": "yes",
            "plugin_title": {"title": "Tutorial image"},
            "fixture_role": "tutorial-image",
        }
    )
    return config


def _ensure_main_plugins(page, image, document, alias, destination_page) -> None:
    from cms.api import add_plugin

    placeholder = _content_placeholder(_current_content(page))
    plugins = placeholder.get_plugins(LANGUAGE)
    container = plugins.filter(plugin_type="GridContainerPlugin").first()
    if container is None:
        container = add_plugin(
            placeholder,
            "GridContainerPlugin",
            LANGUAGE,
            config={
                "container_type": "container",
                "plugin_title": {"title": "Main content"},
            },
        )
    if not plugins.filter(plugin_type="TextPlugin").exists():
        add_plugin(
            placeholder,
            "TextPlugin",
            LANGUAGE,
            target=container,
            body=(
                "<h1>Welcome to the django CMS user guide</h1>"
                "<p>This page provides stable content for automated screenshots.</p>"
            ),
        )
    image_plugin = plugins.filter(plugin_type="ImagePlugin").first()
    # ``cms.api.add_plugin`` stores a supplied JSON config verbatim.  Start
    # with the form defaults so model properties such as ``external_picture``
    # are available when the structure board asks for the plugin's short
    # description. Merge an existing fixture's values as well, which repairs
    # fixtures created by older versions of this script.
    if image_plugin is not None:
        image_instance, _ = image_plugin.get_plugin_instance()
        image_config = _frontend_image_config(image, image_instance.config)
    else:
        image_config = _frontend_image_config(image)
    if image_plugin is None:
        add_plugin(
            placeholder,
            "ImagePlugin",
            LANGUAGE,
            target=container,
            config=image_config,
        )
    elif image_instance.config != image_config:
        image_instance.config = image_config
        image_instance.save(update_fields=["config"])
    frontend_links = []
    for base_plugin in plugins.filter(plugin_type="TextLinkPlugin"):
        instance, _ = base_plugin.get_plugin_instance()
        if instance is not None:
            frontend_links.append(instance)
    if not any(
        plugin.config.get("fixture_role") == "standalone-button"
        for plugin in frontend_links
    ):
        add_plugin(
            placeholder,
            "TextLinkPlugin",
            LANGUAGE,
            target=container,
            config={
                "name": "Learn about our services",
                "link": {
                    "internal_link": f"cms.page:{destination_page.pk}",
                },
                "link_type": "btn",
                "link_context": "primary",
                "fixture_role": "standalone-button",
            },
        )
    if not plugins.filter(plugin_type="Alias").exists():
        add_plugin(
            placeholder,
            "Alias",
            LANGUAGE,
            target=container,
            alias=alias,
        )
    if not any(
        plugin.config.get("fixture_role") == "text-link"
        for plugin in frontend_links
    ):
        text = plugins.filter(plugin_type="TextPlugin").first()
        if text is not None:
            add_plugin(
                placeholder,
                "TextLinkPlugin",
                LANGUAGE,
                target=text,
                config={
                    "name": "Download the guide",
                    "link": {"file_link": document.pk},
                    "fixture_role": "text-link",
                },
            )


def _repair_version_image_plugins(page, image) -> None:
    """Bring image copies in every historical version up to current defaults."""

    for version in _page_versions(page):
        placeholder = _content_placeholder(version.content)
        for plugin in placeholder.get_plugins(LANGUAGE).filter(plugin_type="ImagePlugin"):
            instance, _ = plugin.get_plugin_instance()
            if instance is None:
                continue
            config = _frontend_image_config(image, instance.config)
            if instance.config != config:
                instance.config = config
                instance.save(update_fields=["config"])


def _add_version_note(version, text: str) -> None:
    from cms.api import add_plugin

    placeholder = _content_placeholder(version.content)
    add_plugin(
        placeholder,
        "TextPlugin",
        LANGUAGE,
        body=f"<p>{text}</p>",
    )


def _ensure_version_history(page, user) -> None:
    from django.utils import timezone
    from djangocms_versioning.constants import ARCHIVED, DRAFT, PUBLISHED, UNPUBLISHED
    from djangocms_versioning.models import Version

    if _version_in_state(page, PUBLISHED) is None:
        _version_in_state(page, DRAFT).publish(user)

    if _version_in_state(page, UNPUBLISHED) is None:
        draft = _version_in_state(page, DRAFT)
        if draft is None:
            draft = _version_in_state(page, PUBLISHED).copy(user)
        _add_version_note(draft, "Version two adds services and contact information.")
        draft.publish(user)

    if _version_in_state(page, ARCHIVED) is None:
        draft = _version_in_state(page, DRAFT)
        if draft is None:
            draft = _version_in_state(page, PUBLISHED).copy(user)
        _add_version_note(draft, "This alternative introduction was archived.")
        draft.archive(user)

    if _version_in_state(page, DRAFT) is None:
        draft = _version_in_state(page, PUBLISHED).copy(user)
        _add_version_note(draft, "Draft changes ready for editorial review.")

    versions = _page_versions(page)
    now = timezone.now()
    for index, version in enumerate(versions):
        timestamp = now - timedelta(days=len(versions) - index - 1)
        Version.objects.filter(pk=version.pk).update(
            created=timestamp,
            modified=timestamp + timedelta(hours=2),
        )


def _ensure_german_translation(page, user) -> None:
    from cms.api import create_page_content
    from cms.models import PageContent

    if not PageContent._base_manager.filter(page=page, language="de").exists():
        create_page_content(
            language="de",
            title="Willkommen",
            slug="willkommen",
            menu_title="Willkommen",
            page=page,
            created_by=user,
        )
    _publish_draft(page, user, language="de")


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
    site.save(update_fields=["domain"])

    folder, image, document = _ensure_filer_assets(user)
    alias = _ensure_alias(site, user)

    pages = {}
    for fixture in PAGE_FIXTURES:
        page = _ensure_page(fixture, pages, site, user)
        pages[fixture["reverse_id"]] = page
        if fixture["reverse_id"] != PAGE_REVERSE_ID:
            _ensure_page_text(page, fixture["title"])
        if fixture.get("published"):
            _publish_draft(page, user)

    page = pages[PAGE_REVERSE_ID]
    _ensure_main_plugins(
        page,
        image,
        document,
        alias,
        pages["user-guide-screenshot-services"],
    )
    _ensure_version_history(page, user)
    _repair_version_image_plugins(page, image)
    _ensure_german_translation(page, user)

    print(
        "FIXTURES="
        f"pages:{len(pages)},"
        f"filer_folder:{folder.pk},"
        f"image:{image.pk},"
        f"document:{document.pk},"
        f"alias:{alias.pk},"
        f"versions:{len(_page_versions(page))}"
    )

    return page.get_absolute_url(language=LANGUAGE)


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
