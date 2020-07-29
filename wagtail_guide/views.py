from django.shortcuts import render
from wagtail.core.models import Site

from .models import EditorGuide


def index(request):
    # There should only ever be one instance of the guide
    # But we need to check the site incase there is a 'per' site guide
    # On a multisite setup
    content = EditorGuide.objects.all().filter(
        site=Site.find_for_request(request)
    ).first()

    # Send a boolean to populate a menu if there are more than
    # one 'heading' block type.
    nav = False
    if content:
        if len([i.block_type for i in content.sections if i.block_type=='heading']) > 1:
            nav = True

    return render(request, 'wagtail_guide/base.html', {
        'content': content,
        'nav': nav
    })
