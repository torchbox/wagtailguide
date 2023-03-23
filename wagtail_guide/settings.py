from django.conf import settings


class WagtailGuideSettings:
    def __init__(self, defaults=None):
        self.defaults = {
            "ADD_WAGTAIL_GUIDE_TO_HELP_MENU": False,
            "WAGTAIL_GUIDE_MENU_LABEL": "Editor guide",
            "HIDE_WAGTAIL_CORE_EDITOR_GUIDE": True,
        }
        if defaults is not None:
            self.defaults.update(defaults)

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{attr}'"
            )

        django_settings = getattr(settings, "WAGTAIL_GUIDE_SETTINGS", {})
        return django_settings.get(attr, self.defaults[attr])


wagtail_guide_settings = WagtailGuideSettings()
