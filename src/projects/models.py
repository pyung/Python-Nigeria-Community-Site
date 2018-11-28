from base.blocks import BaseStreamBlock
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


# Create your models here.
class ProjectPage(Page):
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    description = StreamField(BaseStreamBlock(), verbose_name="description")
    links = StreamField(BaseStreamBlock(), verbose_name="links",null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        StreamFieldPanel("description"),
        FieldPanel("start_date"),
        StreamFieldPanel("links"),
    ]

class ProjectIndexPage(Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
    ]

    # Can only have ProjectPage children
    subpage_types = ['ProjectPage']

    # Returns a queryset of ProjectPage objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_projects(self):
        return ProjectPage.objects.live().descendant_of(
            self).order_by('-start_date')

    # Allows child objects (e.g. ProjectPage objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live()

    
    # Pagination for the index page. We use the `django.core.paginator` as any
    # standard Django app would, but the difference here being we have it as a
    # method on the model rather than within a view function
    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_projects(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request):
        context = super().get_context(request)

        # ProjectPage objects (get_breads) are passed through pagination
        breads = self.paginate(request, self.get_projects())
        context['projects'] = breads

        return context
