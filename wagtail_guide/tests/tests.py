from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from ..models import EditorGuide


from wagtail.test.utils import WagtailTestUtils


class EditorGuideTest(TestCase, WagtailTestUtils):
    def setUp(self):
        super().setUp()
        self.login()
        User = get_user_model()
        editors_group = Group.objects.get(name="Editors")

        self.editor = User.objects.create_user(username="testuser", password="pass")
        self.editor.groups.add(editors_group)

    def test_admin(self):
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertEqual(response.status_code, 200)

    def test_guide_edit_links(self):
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertIn(
            '"name": "manage-editor-guide", "label": "Manage Editor Guide"',
            response.content.decode(),
        )

    def test_editor_view(self):
        response = self.client.get(reverse("wagtaileditorguide"))
        self.assertEqual(response.status_code, 200)

    def test_editor_view_null_message(self):
        # Check we see the no create message if no guide is added
        response = self.client.get(reverse("wagtaileditorguide"))
        self.assertContains(
            response,
            '<p class="help-block help-warning">An editor guide has not been\n'
            "created yet. Add one in Settings > Manage Editor Guide</p>",
            html=True,
        )

    def test_adding_a_guide(self):
        # Check we can see field data in the guide once added
        EditorGuide.objects.create(
            information_text="9999",
            sections=[
                ("heading", "A Heading"),
                ("heading", "Another heading"),
            ],
            site_id=1,
        )
        response = self.client.get(reverse("wagtaileditorguide"))
        self.assertContains(response, "A Heading")

    def test_permissions(self):
        # Unless the manage permission guide is added to the editor group,
        # An editor shouldn't be able to see the managle link in settings > manage guide
        self.client.logout()
        self.client.login(username="testuser", password="pass")
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertNotContains(
            response,
            '<a href="/admin/settings/wagtail_guide/editorguide/" class="icon icon-help">Manage Editor Guide</a>',
            html=True,
        )

    def test_applied_settings(self):
        """Testing settings.
        Settings are set in the test settings file and are as follows:
        WAGTAIL_GUIDE_SETTINGS = {
            "ADD_WAGTAIL_GUIDE_TO_HELP_MENU": False,
            "WAGTAIL_GUIDE_MENU_LABEL": "WG guide menu label",
            "HIDE_WAGTAIL_CORE_EDITOR_GUIDE": True,
        }
        We want to test these are applied correctly.
        """

        # Custom guide should show in menu
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertIn(
            '"name": "wg-guide-menu-label", "label": "WG guide menu label"',
            response.content.decode(),
        )
        # Core editor guide should be hidden
        self.assertNotIn(
            '"name": "editor-guide", "label": "Editor Guide"',
            response.content.decode(),
        )
