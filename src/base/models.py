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
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet

from .blocks import BaseStreamBlock

# Create your models here.


@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """

    heading = models.CharField(max_length=255, blank=True)
    body = StreamField(BaseStreamBlock(), verbose_name="Body")

    panels = [FieldPanel("heading"), StreamFieldPanel("body")]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = "Footer Text"


class AbstractPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page Body", blank=True, null=True
    )

    class Meta:
        abstract = True

    content_panels = Page.content_panels + [StreamFieldPanel("body")]


class StandardPage(AbstractPage):
    pass