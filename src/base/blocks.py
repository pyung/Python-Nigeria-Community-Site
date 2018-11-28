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

class LinkBlock(StructBlock):
    url = URLBlock()
    icon = TextBlock()

    class Meta:
        template = "blocks/footer_section.html"

class ProjectBlock(StructBlock):
    link = URLBlock()
    summary = TextBlock()

    class Meta:
        template = "blocks/project_section.html"

class BaseStreamBlock(StreamBlock):
    section_blocks = SectionBlock()
    link = LinkBlock()
    project_link = ProjectBlock()
    paragraph = RichTextBlock(template="blocks/paragraph_block.html")