from django.conf.urls import url
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from . import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^editorguide/$', views.index, name='wagtaileditorguide'),
    ]


@hooks.register('register_admin_menu_item')
def register_editor_guide_menu_item():
    return MenuItem(
        _('Editor guide'),
        reverse('wagtaileditorguide'),
        classnames='icon icon-help',
        order=1000
    )