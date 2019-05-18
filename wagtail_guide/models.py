from django.db import models

from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "wagtail_guide/streamfield/blocks/image_block.html"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.CharBlock(classname="title")
    attribution = blocks.CharBlock(required=False)

    class Meta:
        icon = "openquote"
        template = "wagtail_guide/streamfield/blocks/quote_block.html"


class PullQuoteBlock(blocks.StructBlock):
    pull_quote = blocks.CharBlock(classname="title")

    class Meta:
        icon = "openquote"
        template = "wagtail_guide/streamfield/blocks/pull_quote_block.html"


class IframeBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    source = blocks.URLBlock()

    class Meta:
        icon = "code"
        template = "wagtail_guide/streamfield/blocks/iframe_block.html"


class EmbedTitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    embed = EmbedBlock()

    class Meta:
        icon = "media"
        template = 'wagtail_guide/streamfield/blocks/embed_block.html'


class VideoBlock(blocks.StructBlock):
    video = EmbedBlock(required=False, label='Video URL')

    class Meta:
        icon = "media"
        template = 'wagtail_guide/streamfield/blocks/video_block.html'
        label = "Video"


class GuideBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(
        classname='full title', icon='title',
        template='wagtail_guide/streamfield/blocks/heading_block.html'
    )

    paragraph = blocks.RichTextBlock(features=[
        'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'ul', 'ol', 'hr'])
    image = ImageBlock()
    quote = QuoteBlock()
    pull_quote = PullQuoteBlock()
    embed = EmbedTitleBlock()
    video = VideoBlock()

    class Meta:
        template = "wagtail_guide/streamfield/stream_block.html"


@register_setting(icon="help")
class EditorGuide(BaseSetting, ClusterableModel):
    information_text = models.TextField(
        blank=True, help_text='Add a leading information paragraph explaining the guide')
    sections = StreamField(GuideBlock(required=False), blank=True)

    panels = [
        FieldPanel('information_text'),
        StreamFieldPanel('sections')
    ]

    class Meta:
        verbose_name = 'Manage Editor Guide'
