from django.db import models
from django_prices.models import PriceField
from django.utils.timezone import now
from model_tools.util import TimeStampedModel

class ProductManager(BaseUserManager, InheritanceManager):
    """Not sure we need a manager yet"""
    pass

class ProductGroup(models.Model):
    """Product Groups"""
    group_name = models.CharField(max_length=200)
    group_description = models.CharField(max_length=1000)

    def __str__(self):
        """Return a string representation of the model."""
        return self.group_name


class Product(models.Model, TimeStampedModel):
        product_name = models.CharField(_("Product name"), max_length=255, unique=True)
        product_code = models.CharField(_("Product code"), max_length=255, unique=True)
        unit_price = PriceField(_("Unit price"), currency='NGN', decimal_places=2, max_digits=12, default=0.00)
        product_image = FileField(verbose_name=_("Sample Image"), blank=True, null=True,
            help_text=_("Sample image used in the catalog's list view."))
        description = PlaceholderField("Commodity Details")
        group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, blank=True, null=True)

        objects = ProductManager()

        class Meta:
            app_label = app_settings.APP_LABEL
            verbose_name = _("Product")
            verbose_name_plural = _("Products")

        def __str__(self):
            return self.product_name

        def __unicode__(self):
            return str(self.product_name)

        def get_price(self, request):
            return self.unit_price

        def product_image(self):
            if self.product_image and hasattr(self.product_image, 'url'):
                return self.product_image.url

        def get_absolute_url(self):
            return reverse('product:detail', kwargs={'item_id': self.product_code})
