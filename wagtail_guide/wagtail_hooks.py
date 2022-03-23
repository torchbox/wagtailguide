from django.urls import re_path
from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from . import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^editorguide/$', views.index, name='wagtaileditorguide'),
    ]


@hooks.register('register_admin_menu_item')
def register_editor_guide_menu_item():
    return MenuItem(
        _('Editor guide'),
        reverse('wagtaileditorguide'),
        classnames='icon icon-help',
        order=1000
    )


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/css/wagtailguide.css to the wagtail admin area."""
    return format_html('<link rel="stylesheet" href="{}">', static("css/wagtailguide.css"))
