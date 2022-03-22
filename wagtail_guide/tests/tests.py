from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from wagtail.core.models import Page
from wagtail.tests.utils import WagtailTestUtils
from wagtail.tests.utils.form_data import (inline_formset, nested_form_data,
                                           streamfield)

from ..models import EditorGuide


class EditorGuideTest(TestCase, WagtailTestUtils):

    def setUp(self):
        super().setUp()
        self.login()
        User = get_user_model()
        editors_group = Group.objects.get(name='Editors')

        self.editor = User.objects.create_user(username='testuser', password='pass')
        self.editor.groups.add(editors_group)

    def test_admin(self):
        response = self.client.get(reverse('wagtailadmin_home'))
        self.assertEqual(response.status_code, 200)

    def test_guide_view_links(self):
        response = self.client.get(reverse('wagtailadmin_home'))
        self.assertIn('"name": "editor-guide", "label": "Editor guide"', response.content.decode())

    def test_guide_edit_links(self):
        response = self.client.get(reverse('wagtailadmin_home'))
        self.assertIn('"name": "manage-editor-guide", "label": "Manage Editor Guide"', response.content.decode())

    def test_editor_view(self):
        response = self.client.get(reverse('wagtaileditorguide'))
        self.assertEqual(response.status_code, 200)

    def test_editor_view_null_message(self):
        # Check we see the no create message if no guide is added
        response = self.client.get(reverse('wagtaileditorguide'))
        self.assertContains(response, '<p class="help-block help-warning">An editor guide has not been created yet. Add one in Settings > Manage Editor Guide</p>', html=True)

    def test_adding_a_guide(self):
        # Check we can see field data in the guide once added
        EditorGuide.objects.create(
            information_text='9999',
            sections = [
                ('heading', 'A Heading'),
                ('heading', 'Another heading'),
            ],
            site_id=1
        )
        response = self.client.get(reverse('wagtaileditorguide'))
        self.assertContains(response, 'A Heading')

    def test_permissions(self):
        # Unless the manage permission guide is added to the editor group,
        # An editor shouldn't be able to see the managle link in settings > manage guide
        self.client.logout()
        self.client.login(username='testuser', password='pass')
        response = self.client.get(reverse('wagtailadmin_home'))
        self.assertNotContains(response, '<a href="/admin/settings/wagtail_guide/editorguide/" class="icon icon-help">Manage Editor Guide</a>', html=True)
