from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import BaseStreamBlock

# Create your models here.


class AbstractPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page Body", blank=True, null=True
    )

    class Meta:
        abstract = True

    content_panels = Page.content_panels + [StreamFieldPanel("body")]
