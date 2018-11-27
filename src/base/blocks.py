from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    URLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)


class SectionBlock(StructBlock):
    icon = TextBlock()
    heading = TextBlock()
    content = TextBlock()
    link = TextBlock(required=False)

    class Meta:
        template = "blocks/home_section.html"
        classname = 'section-block col-sm-6'


class BaseStreamBlock(StreamBlock):
    section_blocks = SectionBlock()
