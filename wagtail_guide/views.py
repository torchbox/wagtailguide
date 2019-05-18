from django.shortcuts import render
from .models import EditorGuide


def index(request):
    # There should only ever be one instance of the guide
    content = EditorGuide.objects.all().first()

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