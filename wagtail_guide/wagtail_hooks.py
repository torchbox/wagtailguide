from django.templatetags.static import static
from django.urls import re_path, reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from . import views
from .settings import wagtail_guide_settings


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        re_path(r"^editorguide/$", views.index, name="wagtaileditorguide"),
    ]


if wagtail_guide_settings.ADD_WAGTAIL_GUIDE_TO_HELP_MENU:

    @hooks.register("register_help_menu_item")
    def register_editor_guide_menu_item():
        return MenuItem(
            _(wagtail_guide_settings.WAGTAIL_GUIDE_MENU_LABEL),
            reverse("wagtaileditorguide"),
            classnames="icon icon-help",
            order=1000,
        )

else:

    @hooks.register("register_admin_menu_item")
    def register_editor_guide_menu_item():
        return MenuItem(
            _(wagtail_guide_settings.WAGTAIL_GUIDE_MENU_LABEL),
            reverse("wagtaileditorguide"),
            classnames="icon icon-help",
            order=1000,
        )


if wagtail_guide_settings.HIDE_WAGTAIL_CORE_EDITOR_GUIDE:

    @hooks.register("construct_help_menu")
    def construct_help_menu(request, menu_items):
        items_to_hide = ["https://guide.wagtail.org/"]
        menu_items[:] = [item for item in menu_items if item.url not in items_to_hide]
        return menu_items


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/css/wagtailguide.css to the wagtail admin area."""
    return format_html(
        '<link rel="stylesheet" href="{}">', static("css/wagtailguide.css")
    )
